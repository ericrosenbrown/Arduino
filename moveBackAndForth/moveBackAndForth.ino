#include <Servo.h>

Servo middle;

int middleStart = 0; //The starting servo angle for middle
int middleEnd = 90; //The ending servo angle for middle

void setup() {
  // put your setup code here, to run once:
  middle.attach(11);
}

void loop() {
  scanner();
}

// This will allow the arm to scan back and forth constantly
void scanner() {
  for (int curAngle = middleStart; curAngle < middleEnd; curAngle++)
  {
    middle.write(curAngle);
    delay(10);
  }
  
  for (int curAngle = middleEnd; curAngle > middleStart; curAngle--)
  {
    middle.write(curAngle);
    delay(10);
  }
}
