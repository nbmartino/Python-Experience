#!/usr/bin/python
import struct
import subprocess
import os
inputDevice = "/dev/input/event2"

# format of the event structure (int, int, short, short, int)
inputEventFormat = 'iihhi'
inputEventSize = 16
 
file1 = open(inputDevice, "rb") # standard binary file input
event = file1.read(inputEventSize)

while True:
  (time1, time2, type, code, value) = struct.unpack(inputEventFormat, event)
  if type == 1 and code == 276 and value == 1:
     output = subprocess.check_output(['cat', '/home/ubuntu/RFID/mode'])
     if output == '0\n':        
	os.system("echo 1 > /home/ubuntu/RFID/mode")
	os.system("echo 1 > /sys/class/leds/beagleboard\:\:usr1/brightness")
     else:
        os.system("echo 0 > /home/ubuntu/RFID/mode") 
	os.system("echo 0 > /sys/class/leds/beagleboard\:\:usr1/brightness")	
  event = file1.read(inputEventSize)
file1.close()
