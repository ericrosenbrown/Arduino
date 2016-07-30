String sentence; 
char letters[100]; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);    
}

void loop() {
  if (Serial.available()){
    sentence = Serial.readString(); //Reads in the entire sentence
    Serial.println(sentence);
    //sentence.toCharArray(letters,100); //Turns the sentence into an array of characters, and stores them in letters array
  }
}
