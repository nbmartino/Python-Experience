#!/usr/bin/python
import sys
import os
import time
import usb.core
import usb.util
import usb.backend.libusb1
import operator
import MySQLdb
import struct
import subprocess 


chrMap = {
    4:  'a',
    5:  'b',
    6:  'c',
    7:  'd',
    8:  'e',
    9:  'f',
    10: 'g',
    11: 'h',
    12: 'i',
    13: 'j',
    14: 'k',
    15: 'l',
    16: 'm',
    17: 'n',
    18: 'o',
    19: 'p',
    20: 'q',
    21: 'r',
    22: 's',
    23: 't',
    24: 'u',
    25: 'v',
    26: 'w',
    27: 'x',
    28: 'y',
    29: 'z',
    30: '1',
    31: '2',
    32: '3',
    33: '4',
    34: '5',
    35: '6',
    36: '7',
    37: '8',
    38: '9',
    39: '0',
    40: 'KEY_ENTER',
    41: 'KEY_ESCAPE',
    42: 'KEY_BACKSPACE',
    43: 'KEY_TAB',
    44: ' ',
    45: '-',
    46: '=',
    47: '[',
    48: ']',
    49: '\\',
    51: ';',
    52: '\'',
    53: '`',
    54: ',',
    55: '.',
    56: '/',
    57: 'KEY_CAPSLOCK'
}
def check_mode():
    output = subprocess.check_output(['cat', '/home/ubuntu/RFID/mode'])
    if output == '0\n':
	return 0
    else:
	return 1

def blink(mode): # this is a function, actually...
   for i in range(3):
   # turn on USR2
      os.system("echo 1 > /sys/class/leds/beagleboard\:\:usr1/brightness")
      time.sleep(0.1)
   # turn off USR2
      os.system("echo 0 > /sys/class/leds/beagleboard\:\:usr1/brightness") 
      time.sleep(0.1)
   if mode == 1:
      os.system("echo 1 > /sys/class/leds/beagleboard\:\:usr1/brightness") 
   return

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "/lib/arm-linux-gnueabihf/libusb-1.0.so.0")

# find our device
dev = usb.core.find(idVendor=0x08ff, idProduct=0x0009, backend=backend)

# was it found?
if dev is None:
    raise ValueError('Device not found')

interface = 0
if dev.is_kernel_driver_active(interface) is True:
  # tell the kernel to detach
  dev.detach_kernel_driver(interface)
  # claim the device
  usb.util.claim_interface(dev, interface)

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get device endpoint information
endpoint = dev[0][(0,0)][0]		
count = 0
serial_no = ''

cmd = 'python /home/ubuntu/RFID/readUserButton.py'
subprocess.Popen(cmd, shell = True)

while True:
    try:

        results = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize, 1000)
	count += 1
	
	if results[2] != 40:
	   if count % 2:
	      #print 'count % 2'
	      if results[2] != 0:
	         serial_no +=  chrMap[results[2]]
		 
	elif results[2] == 40:
	   print 'EOL'

	if count == 22:
	   
	   mode = check_mode()

	   # Open database connection
	   db = MySQLdb.connect("localhost","root","12345","RFID")

	   # prepare a cursor object using cursor() method
	   cursor = db.cursor()
	   count=0

	   output = subprocess.check_output(['cat', '/home/ubuntu/RFID/mode'])
     	   if mode == 0:
              print 'Mode = Aunthenticate\n'
	      sql = """SELECT COUNT(1) FROM CARDS WHERE SERIAL_NO = "%s" """ % (serial_no)
	      cursor.execute(sql)
	      if cursor.fetchone()[0]:
	         print 'PASSED!\n'
		 blink(mode)
	      else:
	         print 'FAILED!\n'
	   else: #if mode = 1
 	      print 'Mode=Register\n'
	      sql = """INSERT INTO CARDS (SERIAL_NO) VALUES ("%s")""" % (serial_no)
	      try:
   	         # Execute the SQL command
                 cursor.execute(sql)
                 # Commit your changes in the database
                 db.commit()
	         print serial_no + ' is now registered!'
		 blink(mode)   
	      except MySQLdb.Error, e:
  	         print "Error %d: %s" % (e.args[0], e.args[1])
   	         # Rollback in case there is any error
                 db.rollback()
        
	   cursor.close()
	   db.close()
	   serial_no = ''

    except usb.core.USBError as e:
        if e.args[1] == 'Operation timed out':
	    print 'waiting for input...'
            #break # timeout and swiped means we are done

file.close

