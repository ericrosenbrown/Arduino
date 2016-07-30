int const hPin = A1; //Horizontal control
int const vPin = A1; //Vertical control
int potVal;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int hVal = analogRead(hPin);
  int vVal = analogRead(vPin);
  Serial.print(hVal);
  Serial.print(" ");
  Serial.println(vVal);
  delay(100);
} 
