
int A = 0;
int B = 0;
int Bprev = 0;

// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;
// Motor B connections
int enB = 3;
int in3 = 5;
int in4 = 4;


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
  Serial.begin(9600);
}
void loop() {
A = Serial.parseInt();//input from serial
if(A!=0){
  Bprev = B;
  B=A;
  direc = B;
  /*for (int i = Bprev ; i < B; i++) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  for (int i = Bprev ; i > B; i--) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  */
}
if (direc > 4 || direc < 0){
  direc = 0;
}
Serial.println(B);

//analogWrite(enA, B);
//analogWrite(enB, B);
analogWrite(enA, 128);
analogWrite(enB, 128);

if(direc == 0){

  for (int i = 128; i > 0; i--) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
    for (int i = 0  ; i < 128; i++) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}
else if(direc == 1){
    for (int i = 128; i > 0; i--) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
    for (int i = 0  ; i < 128; i++) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}
else if(direc == 2){
    for (int i = 128; i > 0; i--) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
    for (int i = 0  ; i < 128; i++) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}
else if(direc == 3){
    for (int i = 128; i > 0; i--) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
    for (int i = 0  ; i < 128; i++) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}
else if(direc == 4){
    for (int i = 128; i > 0; i--) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
    for (int i = 0  ; i < 128; i++) {
    analogWrite(enA, i);
    analogWrite(enB, i);
    delay(20);
  }
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, HIGH);
  delay(500);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

delay(10); 
}
