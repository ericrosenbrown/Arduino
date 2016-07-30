const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  float sensorValue = analogRead(sensorPin);
  float dimmerValue = map(sensorValue,750,950,0,10);
  dimmerValue = dimmerValue;
  //Serial.print("Sensor Value: ");
  //Serial.print(sensorValue);
  //Serial.print("Dimmer Value: ");
  Serial.println(dimmerValue);
  delay(200);
}
