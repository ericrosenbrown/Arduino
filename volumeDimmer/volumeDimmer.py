import serial
import time
import os
import subprocess

ser = serial.Serial('/dev/tty.usbmodem1411',9600)
time.sleep(2)
print("Starting...")
while True:
    dimValue = ser.readline()
    print(dimValue)
    os.system("osascript -e \"set Volume "+dimValue+"\"")
