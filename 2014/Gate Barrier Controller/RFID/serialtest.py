import serial

port=serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=3.0)

while True: 
   port.write("a")
   rcv=port.read(1)
   print repr(rcv)

