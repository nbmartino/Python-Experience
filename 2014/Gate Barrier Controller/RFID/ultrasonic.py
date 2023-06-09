import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

TRIG=17
ECHO=18

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
while True:
 try:
   GPIO.output(TRIG,False)
   print "Waiting for sensor to settle"
   time.sleep(1)
   GPIO.output(TRIG,True)
   time.sleep(0.00001)
   GPIO.output(TRIG,False)

   while GPIO.input(ECHO)==0:
      pulse_start=time.time()

   while GPIO.input(ECHO)==1:
      pulse_end=time.time()

   pulse_duration=pulse_end-pulse_start

   distance=pulse_duration * 17150
   distance=round(distance,2)
   print "Distance:",distance,"cm"
   

 except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit(0)
