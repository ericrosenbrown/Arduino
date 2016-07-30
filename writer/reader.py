import serial
import time

ser = serial.Serial('/dev/tty.usbmodem1411',9600)
time.sleep(2)
print("starting")
while True:
    print ser.readline()
    #ser.write('hello me')
    
