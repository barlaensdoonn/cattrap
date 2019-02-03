#!/usr/bin/python3

from time import sleep
from datetime import datetime
from collections import deque
from gpiozero import DistanceSensor


def check_curfew(start=21, stop=9):
    now = datetime.now()
    if now.hour >= start or now.hour <= stop:
        return True
    else:
        return False


def roll():
    vals = deque()
    while True:
        val = yield
        if len(vals) < 10:
            vals.append(val)
        if len(vals) == 10:
            vals.popleft()
            vals.append(val)
        yield sum(vals) / len(vals)


if __name__ == '__main__':
    sensor = DistanceSensor(echo=4, trigger=5)

    while True:
        run = check_curfew()

        while run:
            print('distance: {}'.format(sensor.distance))
        
            if sensor.distance <= 0.5:
                print('i see you')
                # spray the cat
        
            sleep(0.25)
            run = check_curfew()

        time.sleep(1)
