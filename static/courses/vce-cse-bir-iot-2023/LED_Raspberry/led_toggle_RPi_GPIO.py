# Program to demonstrate blinking of a LED
# Using RPi.GPIO package

import RPi.GPIO as GPIO
import time

# Intialize LED to connected (logical)pin on board - refer pinout command
GPIO.setmode (GPIO.BCM)
GPIO.setup (4, GPIO.OUT)

# to intialize LED to connected Physical pin on board use:
# GPIO.setmode (GPIO.BOARD)

while True:
   # switch led on
   GPIO.output (4, True)
   time.sleep (3)
   # switch led off
   GPIO.output (4, False)
   time.sleep (1)