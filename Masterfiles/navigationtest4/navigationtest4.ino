//declace a String to hold what we're inputting
String incomingString;

//Motor vars
int A = 0;
int B = 0;
int Bprev = 0;
int Aprev = 0;

// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;
// Motor B connections
int enB = 3;
int in3 = 4;
int in4 = 5;

int mtdirec[4] = {1,1,1,1};

int direc = 0;//f = 0,b = 1, l = 2, r = 3, s = 4

void setup() {
    // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 0);
  analogWrite(enB, 0);
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
  Aprev = A;
  Bprev = B;
  A = value1.toInt();
  B = value2.toInt();
  motor(enA, in1, in2, A ,Aprev);
  motor(enB, in3, in4, B ,Bprev);
  //Serial.println(A);
 // Serial.println(B);
   

} 

}
//motor(enA, in1, in2, A ,Aprev)
//motor(enB, in3, in4, B ,Bprev)
void motor(int mtc, int drc1, int drc2, int neew, int oold){
  int ramp = 1;
  if(neew > 0 && oold <= 0){
    analogWrite(mtc,0);
    digitalWrite(drc2, HIGH);
    digitalWrite(drc1, LOW);
    analogWrite(mtc,neew);
    
  }
  else if(neew < 0 && oold >= 0){
    analogWrite(mtc,0);
    digitalWrite(drc2, LOW);
    digitalWrite(drc1, HIGH);
    analogWrite(mtc,-neew);
    
  } else if(abs(neew) > abs(oold)){
      analogWrite(mtc,abs(neew));
      Serial.println(neew);
  } else if(abs(neew) < abs(oold)){
      analogWrite(mtc,abs(neew));
     
  }
  Serial.println(neew);
}
