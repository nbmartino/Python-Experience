import smbus
import time
import subprocess

bus = smbus.SMBus(1)

address  = 0x08



while True:
 try:
   bus.write_byte(0x08,5)
   time.sleep(0.05)
 except IOError:
   subprocess.call(['i2cdetect','-y','1'])
   flag = 1
