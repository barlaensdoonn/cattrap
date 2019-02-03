#!/usr/bin/python3

from time import sleep
from datetime import datetime
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=4, trigger=5)


def check_curfew(start=21, stop=9):
    now = datetime.now()
    if now.hour >= start or now.hour <= stop:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        run = check_curfew()

        while run:
            print('Distance: ', sensor.distance * 100)
        
            if sensor.distance <= 0.5:
                print('i see you')
                # spray the cat
        
            sleep(0.25)
            run = check_curfew()

