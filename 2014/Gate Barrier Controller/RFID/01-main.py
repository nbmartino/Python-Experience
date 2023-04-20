#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
import time
import os
import sys
import MySQLdb
import serial

from evdev import device,util,ecodes
from select import select


#ser = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=1)
#ser.flushInput();

keys = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

def printFunction(channel):
   if GPIO.input(13) == 1:
      GPIO.output(13, 0)
   else:
      GPIO.output(13, 1)

def exportPin(pinnum, direction, initval):
   if os.path.exists('/sys/class/gpio/gpio' + str(pinnum) ) != True :
      os.system('echo ' + str(pinnum) + ' > /sys/class/gpio/export')
      os.system('echo "' + direction + '" > /sys/class/gpio/gpio' + str(pinnum) + '/direction')
      #if direction == 'out':
      os.system('echo ' + str(initval) + ' > /sys/class/gpio/gpio' + str(pinnum) + '/value')

def blink(pinnum):
#   initval = GPIO.input(pinnum)
#   for i in range(3):
#      GPIO.output(pinnum,1)#os.system('echo 1 > /sys/class/gpio/gpio' + str(pinnum) + '/value')
#      time.sleep(0.1)
#      GPIO.output(pinnum,0)#os.system('echo 0 > /sys/class/gpio/gpio' + str(pinnum) + '/value') 
#      time.sleep(0.1)
   GPIO.output(pinnum,1)#os.system('echo 1 > /sys/class/gpio/gpio' + str(pinnum) + '/value')
   time.sleep(0.2)
   GPIO.output(pinnum,0)#os.system('echo 0 > /sys/class/gpio/gpio' + str(pinnum) + '/value') 

#   GPIO.output(pinnum, initval)
def SignalOpenGate():
   GPIO.output(21,1)
   time.sleep(1)
   GPIO.output(21,0)  

# export GPIO pins if not exported
exportPin(27,'in',0)
exportPin(13,'out',0)
exportPin(19,'out',0)
exportPin(6,'out',0)
exportPin(29,'out',0)
exportPin(21,'out',0)

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #
GPIO.setup(27, GPIO.IN) # input pin: toggle pin for switching Authentication/Registration mode
GPIO.setup(13, GPIO.OUT) # indicator pin: ON=Registration mode, OFF=Authentication mode
GPIO.setup(19, GPIO.OUT) # indicator pin: error, Authentication/Registration not successful
GPIO.setup(6, GPIO.OUT) # indicator pin: Registration successful
GPIO.setup(29, GPIO.OUT) #
GPIO.setup(21, GPIO.OUT) # signal to psoc to open gate

GPIO.add_event_detect(27, GPIO.RISING, callback=printFunction, bouncetime=300)

# Open database connection
db = MySQLdb.connect("localhost","root","12345","RFID")
# prepare a cursor object using cursor() method


cmd = '/home/pi/BIO/bin/pi/auto_on_fdu05' #location of c program for fingerprint scanner, based of secure metrics example
#proc = subprocess.Popen(cmd, shell = True)
devices = map(device.InputDevice, ('/dev/input/event0','/dev/input/event1'))
devices = {dev.fd : dev for dev in devices}
for dev in devices.values(): print(dev)
serial_no = ''

while True:
   r,w,x = select(devices,[],[])
   try:
    for fd in r:
      for event in devices[fd].read():  
	    if event.type == ecodes.EV_KEY:  # see Evdev documentation
       	       data = util.categorize(event)
               if data.keystate == 1 and data.scancode != 42: # Catch only keydown, and not Enter
                  if data.scancode != 28:
                     serial_no += keys[data.scancode]
                  else:
		     cursor = db.cursor()
                     print serial_no
		     if GPIO.input(13) == 0:  # authentication mode
		        print 'Mode = Auth\n'
       			sql = """SELECT COUNT(1) FROM CARDS WHERE serial_no = "%s" AND enabled = 1 """ % (serial_no)
       			cursor.execute(sql)
       			if cursor.fetchone()[0]:
	  		   blink(6)
			   SignalOpenGate()
			   print 'Passed: %s\n' % serial_no
	  		   
       			else:
	  		   print 'Failed: %s\n' % serial_no
			   blink(19)
		     else:
			print 'Mode =  Reg\n'
       			sql = """INSERT INTO CARDS (serial_no) VALUES ("%s")""" % (serial_no)
       			try:
          		   # Execute the SQL command
          		   cursor.execute(sql)
          		   # Commit your changes in the database
          		   db.commit()
	  		   print 'Registered: %s\n' % serial_no
	  		   blink(6)
		    	except MySQLdb.Error, e:
  	  		   print "Error %d: %s" % (e.args[0], e.args[1])
   	  		   # Rollback in case there is any error
          		   db.rollback()
			   blink(19)
   		     cursor.close()
		     serial_no = ""
		     
   except KeyboardInterrupt:
      
      db.close()
#      proc.kill()
      sys.exit(0)


