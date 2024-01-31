# 링비트 주행과 멈춤
from microbit import *
from Ringbit import RINGBIT

car = RINGBIT(pin1, pin2)

while True:
    if pin_logo.is_touched():
        car.set_motors_speed(100, 100)
        display.scroll('Go')

    if accelerometer.was_gesture('face up'):
        car.set_motors_speed(0, 0)
        display.scroll('Stop')
