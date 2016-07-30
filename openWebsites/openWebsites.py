import serial
import time
import os

ser = serial.Serial('/dev/tty.usbmodem1411',9600)
time.sleep(2)
print("starting")
while True:
    trigger = ser.readline()
    print("===\n"+trigger+"\n=====")
    if trigger:
        print("attempt")
        os.system("open https://www.arduino.cc")
        os.system("open https://www.wikipedia.org")
        os.system("open https://www.youtube.com")
        os.system("open https://www.brown.edu")
        os.system("open http://h2r.cs.brown.edu")
        os.system("open https://docs.python.org/3.5//c-api/index.html")
        os.system("open http://www.wolframalpha.com")
    #ser.write('hello me')
    
