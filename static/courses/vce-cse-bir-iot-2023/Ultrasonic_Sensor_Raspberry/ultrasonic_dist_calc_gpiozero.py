# Program to measure the distance of an object
# Ultrasonic ranging module HC - SR04 provides 2cm - 400cm non-contact measurement function
# Wire connecting direct as following:
# 5V Supply
# Trigger Pulse Input - Here GPIO4
# Echo Pulse Output - Here GPIO14
# Ground

from gpiozero import DistanceSensor
import time
sensor = DistanceSensor(trigger=4, echo=14)
while True:
	#using inbuilt distance attribute from the gpiozero package
	distance = sensor.distance * 100
	print("Object is:", distance, "cms away from sensor")
	time.sleep(0.2)
