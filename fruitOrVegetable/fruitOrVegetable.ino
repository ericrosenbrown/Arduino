// the setup routine runs once when you press reset:
char c;
void setup() {                
  // initialize the serial in 19200 baud rate
  Serial.begin(9600);    
  pinMode(2,OUTPUT); //Vegetable
  pinMode(4,OUTPUT); //Fruit
  pinMode(7,OUTPUT);  //Other
}

// the loop routine runs over and over again forever:
void loop() {
  delay(200);               // wait for a second
  if (Serial.available()){
    c = Serial.read();
    if (c == 'f'){
      digitalWrite(2,LOW);
      digitalWrite(4,HIGH);
      digitalWrite(7,LOW);
      
    }
    else if(c == 'v'){
      digitalWrite(2,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(7,LOW);
    }
    
    else if(c == 'o'){
      digitalWrite(2,LOW);
      digitalWrite(4,LOW);
      digitalWrite(7,HIGH);
    }
  // Serial.println(c);
  }
}
