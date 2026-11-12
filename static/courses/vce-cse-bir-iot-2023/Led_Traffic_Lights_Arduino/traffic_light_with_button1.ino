// Traffic Lights demo with push button
int buttonState = 0;
void setup()
{
  pinMode(2, INPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}
// pin 13 REd
// pin 12 Yellow
// pin 11 Green
void loop()
{
  buttonState = digitalRead(2);
  if (buttonState == HIGH){
    delay(15);
    if (buttonState == HIGH){
      digitalWrite(13, HIGH);
      digitalWrite(12, LOW);
      digitalWrite(11, LOW);
      delay(2000);
      digitalWrite(13, LOW);
      digitalWrite(12, HIGH);
      digitalWrite(11, LOW);
      delay(2000);
      digitalWrite(13, LOW);
      digitalWrite(12, LOW);
      digitalWrite(11, HIGH);
      delay(2000);
    }
  }
}