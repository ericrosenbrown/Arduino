import serial
import urllib2
import time

ser = serial.Serial('/dev/tty.usbmodem1411',9600)
time.sleep(2)
print("starting")
while True:
    #print ser.readline()
    food = raw_input("What food do you want to know about?")
    try:
        link = urllib2.urlopen("https://en.wikipedia.org/wiki/"+food)
        linkContent = link.read()
        fruitCount = linkContent.count("fruit")
        vegeCount = linkContent.count("vegetable")
        if fruitCount > vegeCount:
            ser.write("f")
            #print("Fruit!")
            #print(str(fruitCount)+"\n")
        elif vegeCount > fruitCount:
            ser.write("v")
            #print("Vegetable!")
            #print(str(vegeCount)+"\n")
        else:
            ser.write("o")
            #print("Equally fruitty as veggy")
    except:
        print("Not a wiki page!")
        
    #ser.write('hello me')
    
