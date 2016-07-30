//This is connected to the ledController.py to communciate from python to arduino.
//There should be a LED in digital pin 13. Running the ledController.py will prompt to type a or b.
//a turns on the LED, b turns it off.
// the setup routine runs once when you press reset:
char c;
void setup() {                
  // initialize the serial in 19200 baud rate
  Serial.begin(9600);    
  pinMode(13, OUTPUT); 
}

// the loop routine runs over and over again forever:
void loop() {
  delay(200);               // wait for a second
  if (Serial.available()){
    c = Serial.read();
    if (c == 'a'){
      Serial.println(c);
      digitalWrite(13, HIGH);
    }
    else if (c == 'b'){
      digitalWrite(13,LOW); 
    }
    //Serial.println(c); 
  // Serial.println(c);
  }
}
