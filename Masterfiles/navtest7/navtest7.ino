//PROPERTY OF LUCA GACY -IF YOU SHARE THIS WITHOUT ASKING I WILL END YOU
//...lmao jk spread the love if anyone needs it though most people did their motor code in pytho so I guess it doesn't really matter
//If you're reading this I hope you are having an amazing day!
//this is my ramping code that I finally got to work while watching many episodes of You and 30 Rock and yes one of those is much better than the other

//declace a String to hold what we're inputting
String incomingString;

//Motor vars
int A = 0;//PWM for motor 1
int B = 0;//PWM for motor 2
int Bprev = 0;//previous B - a more OCD person would swap this with the line below...fight me
int Aprev = 0;// previous A

// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;
// Motor B connections
int enB = 3;
int in3 = 5;
int in4 = 4;

int neew = 0;//for gettings abs val of A
int oold = 0;//for getting abs val of Aprev
int s1 = 0;//Are A and Aprev different signs?

int neew2 = 0;//for getting abs val of B
int oold2 = 0;//for getting abs val of Bprev
int s2 = 0;//A B and Bprev different signs?

double ramp = .05;//how fast does it ramp to the stuff
  
int mtdirec[4] = {1,1,1,1};//DELETE ME!!!!!! I'm a useless piece of shit...the code that is

int direc = 0;//f = 0,b = 1, l = 2, r = 3, s = 4 aaaaaannnnddd this is like an appendix...not needed anymore...also what does the appendix even do?

void setup() {
    // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // Turn off motors - Initial state
  digitalWrite(in2, HIGH);
  digitalWrite(in1, LOW);
  digitalWrite(in3, HIGH);
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
//not gonna lie there is a lot of shit below that is kinda like the large part of my prius...I have no idea what is going on but it works and I don't touch it
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
  Aprev = A;//previous value stored
  Bprev = B;
  A = value1.toInt();//this shit like actually gets the values or something
  B = value2.toInt();
  //Serial.println(A);
  //Serial.println(B);
  
  if(A == 0){//lowkey a bunch of shit started breaking when I sent 0 so rather than fixing it in a good way I just pushed the problem under the rug
    A = -1;
  }
  if(B == 0){
    B = -1;
  }
  if(A > 255){
    A = 255;
  }
  if(B > 255){
    B = 255;
  }
  
  neew = abs(A);//OOHHHH boi it's setting up! we about to be rampin!
  oold = abs(Aprev);//my god is this show good
  neew2 = abs(B);//something about sconces...is that even how you spell that word?
  oold2 = abs(Bprev);
  s1 = swap(A,Aprev);
  s2 = swap(B,Bprev);
  
  for(int i = 255; i >= 0; i--){//count down to zero
    if(!s1 && i >= neew && i < oold){//count down ifiifffffiiifffff neew is larger than oold and swap1 wasn't triggered 
      analogWrite(enA, i);
      Serial.print("A ");//my horse's name is trigger
      Serial.println(i);
      delay(ramp);
    }
    if(s1 && oold >= i){//if swap1 is triggered then count down to zero to bounce and swap pins for directions
      analogWrite(enA, i);
      Serial.print("A ");
      Serial.println(i);
      delay(ramp);
    }

    if(!s2 && i >= neew2 && i < oold2){//same shit as above so just feel free to read above at least 900 times while eating cheese pizza 
      analogWrite(enB, i);
      Serial.print("B ");
      Serial.println(i);
      delay(ramp);
    }
    if(s2 && oold2 >= i){
      analogWrite(enB, i);
      Serial.print("B ");
      Serial.println(i);
      delay(ramp);
    }
    //delay(ramp);
  }
  
  if(s1 && A > 0){//swa
    digitalWrite(in2, HIGH);
    digitalWrite(in1, LOW);
    Serial.println("A switching to forward");
  }
  if(s1 && A < 0){
    digitalWrite(in2, LOW);
    digitalWrite(in1, HIGH);
    Serial.println("A switching to backward");
  }

  if(s2 && B > 0){
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    Serial.println("B switching to forward");
  }
  if(s2 && B < 0){
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    Serial.println("B switching to backward");
  }
  for(int i = 0; i <= 255; i++){
    if(!s1 && i <= neew && i > oold){ 
      analogWrite(enA, i);
      Serial.print("A ");
      Serial.println(i);
      delay(ramp);
    }
    if(s1 && neew >= i){
      analogWrite(enA, i);
      Serial.print("A ");
      Serial.println(i);
      delay(ramp);
    }

    if(!s2 && i <= neew2 && i > oold2){ 
      analogWrite(enB, i);
      Serial.print("B ");
      Serial.println(i);
      delay(ramp);
    }
    if(s2 && neew2 >= i){
      analogWrite(enB, i);
      Serial.print("B ");
      Serial.println(i);
      delay(ramp);
    }
    //delay(ramp);
  }
  if(A == 0){
    analogWrite(enA, 0);
    Serial.println(0);
  }
  if(B == 0){
    analogWrite(enB, 0);
    Serial.println(0);
  }
  Serial.println();
  Serial.println(s1);
  Serial.println(s2);
  Serial.println();
  
} 

}

int swap(int n, int o){
  int b = n/abs(n);
  int a = o/abs(o);
  if(a - b == 0){
    return 0;
  } else{
    return 1;
  }
}
