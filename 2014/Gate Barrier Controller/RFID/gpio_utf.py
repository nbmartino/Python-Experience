#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
import time
import os

from evdev import device,util,ecodes
from select import select

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
      os.system('echo ' + str(initval) + ' > /sys/class/gpio/gpio' + str(pinnum) + '/value')


# export GPIO pins if not exported
exportPin(23,'in',0)
exportPin(13,'out',0)
exportPin(19,'out',0)
exportPin(29,'out',0)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=300)
flip=False
cmd = '/home/pi/BIO/bin/pi/auto_on_fdu05'
proc = subprocess.Popen(cmd, shell = True)
dev = InputDevice('dev/input/event0')
print(dev)
while True:
   try:
      flip!=flip
      for event in dev.read_loop():
         if event.type == ecodes.EV_KEY:
       	    data = util.categorize(event)
            if data.keystate == 1 and data.scancode != 42: # Catch only keydown, and not Enter
                  if data.scancode != 28:
                     barcode += keys[data.scancode]
                  else:
                     print barcode
                     barcode = ""

   except KeyboardInterrupt:
      proc._cleanup()
      sys.exit(0)


