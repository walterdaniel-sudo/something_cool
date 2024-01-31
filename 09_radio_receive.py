# 수신
from microbit import *
from Ringbit import RINGBIT
import radio

car = RINGBIT(pin1, pin2)

radio.config(group=1)
radio.on()

while True:
    message = radio.receive()
    if message == '1':
        car.set_motors_speed(30, 30)
        display.show('1')
    elif message == '2':
        car.set_motors_speed(0, 0)
        display.show('2')
