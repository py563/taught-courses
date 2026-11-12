// C++ code
int value=0;

void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(A0, INPUT);
}

void loop()
{
  //reading value photo resistor ldr value
  value=analogRead(A0);
  //guessing 200 is low or dark
  if(value<200)
  {
    Serial.print("Room is dark switching on light: ");
    Serial.println(value);
    digitalWrite(2, HIGH);
  }
  else
  {
    Serial.print("Room is bright switching off light: ");
    Serial.println(value);
    digitalWrite(2, LOW);
  }  
}