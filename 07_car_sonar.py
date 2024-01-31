from microbit import *
from Ringbit import RINGBIT

car = RINGBIT(pin1, pin2)

while True :
    distance = int(car.get_distance())
    display.scroll(distance)
    sleep(200)

    if distance < 60:
        car.set_motors_speed(0, 0)
        display.scroll('Stop')

    else :
        car.set_motors_speed(50, 50)





