import serial
import time
import turtle

ser = serial.Serial('/dev/tty.usbmodem1411',9600)
time.sleep(2)
print("starting")

myTurtle = turtle.Turtle()

vSign = 1 #Positive Direction
hSign = 1 #Positive Direction

##holder = ser.readline()
##l = holder.split(" ")
##hVal = int(l[0])
##vVal = int(l[1])
##
##hChange = hVal - 500
##vChange = vVal - 500
##if hChange > 0:
##    hSign = 1 #Positive Direction
##else:
##    hSign = 0 #Negative direction
##if vChange > 0:
##    vSign = 1 #Positive Direction
##else:
##    vSign = 0 #Negative direction

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

while True:
    #myTurtle.forward(1)
    holder = ser.readline()
    l = holder.split(" ")
    hVal = int(l[0])
    vVal = int(l[1])

    hChange = hVal
    hChange = translate(hVal,0,1023,-10,10)
    vChange = translate(vVal,0,1023,-10,10)
    #print(hChange)
    print(vChange)

    if hChange > 0 and hSign == 1: #Was going positive, still going positive
        myTurtle.forward(hChange)
    elif hChange > 0 and hSign == 0:#Was going negative, now going positive 
        myTurtle.right(180)
        myTurtle.forward(hChange*-1)
        hSign = 1
    elif hChange < 0 and hSign == 1: #Was going positie, now going negative
        myTurtle.right(180)
        myTurtle.forward(hChange*-1)
        hSign = 0
    elif hChange < 0 and hSign == 0: #Was going negative, now going negative
        myTurtle.forward(hChange*-1)

##    if vChange > 0 and vSign == 1: #Was going positive, still going positive
##        myTurtle.left(90)
##        myTurtle.forward(vChange)
##        time.sleep(1)
##        myTurtle.right(90)
##    elif vChange > 0 and vSign == 0:#Was going negative, now going positive 
##        myTurtle.left(90)
##        myTurtle.forward(vChange*-1)
##        time.sleep(1)
##        myTurtle.right(90)
##        vSign = 1
##    elif vChange < 0 and vSign == 1: #Was going positie, now going negative
##        myTurtle.right(90)
##        myTurtle.forward(vChange*-1)
##        time.sleep(1)
##        myTurtle.left(90)
##        vSign = 0
##    elif vChange < 0 and vSign == 0: #Was going negative, now going negative
##        myTurtle.right(90)
##        myTurtle.forward(vChange*-1)
##        time.sleep(1)
##        myTurtle.left(90)
##    time.sleep(1)
    
    #ser.write('hello me')


