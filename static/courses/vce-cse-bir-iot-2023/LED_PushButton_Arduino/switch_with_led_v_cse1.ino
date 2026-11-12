// C++ code
//
/*
  Turn ON / OFF LED using Push Button
*/

int buttonstate = 0;

void setup()
{
  pinMode(2, INPUT);
  pinMode(13, OUTPUT);
}

void loop()
{
  // Initialize Button state with LOW or 0
  buttonstate = 0;
  // Read State of Pin number 2
  buttonstate = digitalRead(2);
  if (buttonstate == 1) {
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(13, HIGH);
    delay(5000); // Wait for 5000 millisecond(s)
  } else {
    digitalWrite(13, LOW);
  }
}