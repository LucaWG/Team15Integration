//declace a String to hold what we're inputting
String incomingString;

void setup() {
  //initialise Serial communication on 9600 baud
  Serial.begin(9600);
  while(!Serial);
  //delay(4000);
  Serial.println("Ready!");
  // The incoming String built up one byte at a time.
  incomingString = "";
}

void loop () {
if(Serial.available()){
  String rxString = "";
  String strArr[2]; //Set the size of the array to equal the number of values you will be receiveing.

  //Keep looping until there is something in the buffer.
  while (Serial.available()) {
    //Delay to allow byte to arrive in input buffer.
    delay(2);
    //Read a single character from the buffer.
    char ch = Serial.read();
    //Append that single character to a string.
    rxString+= ch;
  }

  int stringStart = 0;
  int arrayIndex = 0;

  for (int i=0; i < rxString.length(); i++){
    //Get character and check if it's our "special" character.
    if(rxString.charAt(i) == ','){
      //Clear previous values from array.
      strArr[arrayIndex] = "";
      //Save substring into array.
      strArr[arrayIndex] = rxString.substring(stringStart, i);
      //Set new string starting point.
      stringStart = (i+1);
      arrayIndex++;
    }
  }

  //Put values from the array into the variables.
  String value1 = strArr[0];
  String value2 = strArr[1];

  //Convert string to int if you need it.
  int intValue1 = value1.toInt();
   // Serial.print("test");
    //Serial.print(rxString);
    Serial.print(value1 + " ");
    Serial.print(value2 + "\n");

} 

}
