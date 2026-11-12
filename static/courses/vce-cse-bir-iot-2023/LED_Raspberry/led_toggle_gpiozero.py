# Program to demonstrate blinking of a LED

from gpiozero import LED
import time

# Intialize LED to connected (logical)pin on board - refer pinout command
led = LED(4)

#looping through infinity excepts keyboard interrupt from user 
while True:
  # change led state either on or off
  led.toggle()
  time.sleep(2)
  # change led state from previous
  led.toggle()
  time.sleep(1)