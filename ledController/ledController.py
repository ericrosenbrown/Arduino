import serial
import time

ser = serial.Serial('/dev/tty.usbmodem1411',9600)
time.sleep(2)
print("starting")
while True:
    letter = raw_input('type a or b')
    if letter == 'a' or letter == 'b':
        ser.write(letter)
    #print ser.readline()
    #ser.write('hello me')
    
