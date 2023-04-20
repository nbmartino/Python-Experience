import RPi.GPIO as GPIO
import time
import sys
from array import array

GPIO.setmode(GPIO.BCM)

TRIG=17
ECHO=18

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12, False)
d=[0,0,0,0]
ctr=0
avg=0
while True:
 try:
   GPIO.output(TRIG,False)
#   print "Waiting for sensor to settle"
   time.sleep(0.1)
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
#   if ctr < 4:
#     d[ctr]=distance
#     ctr+=1
 #  else:
#      avg=(d[0]+d[1]+d[2]+d[3])/4
   print "Distance:",distance,"cm"
#      ctr=0
   if distance < 100:
      GPIO.output(12,True)
   else:	
      GPIO.output(12,False);   

 except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit(0)
