# python program to monitor temperature and humidty using DHT sensor on Raspberry Pi3
# using Adafruit-DHT package so check whether package supports raspb4 board else add BCM2711

import Adafruit_DHT
import time

#declaring and setting pins for DHT
DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN=4

while True:
    humidity,temp=Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
    print(humidity,temp)
    if humidity is not None and temp is not None:
        # 0.02f used to print float value to 2 decimal points 
        print(f"Humidity= {humidity:.02f}")
        print(f"Temperature= {temp:.02f}°C")
        time.sleep(3)