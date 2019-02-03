#!/usr/bin/python3

from time import sleep
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=4, trigger=5)

while True:
        print('Distance: ', sensor.distance * 100)
        
        if sensor.distance <= 0.5:
            print('i see you')
            # spray the cat
        
        sleep(0.25)

