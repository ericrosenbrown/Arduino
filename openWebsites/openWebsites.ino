const int piezo = A0;
long counter = millis();
long clapCount = 0;
const int trigger = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  float piezoVal = analogRead(piezo);
  if (clapCount == 2){
   Serial.println("o");
   //Serial.println(counter);
   clapCount = 0; 
   counter = millis();
  }
  else if (piezoVal > trigger && millis()-counter < 1000){
  //Serial.println(piezoVal);
    //Serial.print("Heard a clap (IF)!");
    //Serial.println(counter);
    clapCount++;
    counter = millis();
    delay(10);
  }
  else if(piezoVal > trigger && millis()-counter >=1000){
    //Serial.print("Heard a clap(ELIF)!");
    //Serial.println(counter);
    clapCount = 1;
    counter = millis();
   delay(10); 
   
  }
  //Serial.println(counter);
  // put your main code here, to run repeatedly:

}
