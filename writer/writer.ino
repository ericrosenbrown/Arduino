// the setup routine runs once when you press reset:
char c;
void setup() {                
  // initialize the serial in 19200 baud rate
  Serial.begin(9600);     
}

// the loop routine runs over and over again forever:
void loop() {
  delay(200);               // wait for a second
  Serial.println("hello");
  //if (Serial.available()){
  // c = Serial.read();
   //Serial.println(c); 
  // Serial.println(c);
  //}
}
