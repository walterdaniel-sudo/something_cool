from microbit import *
from Ringbit import RINGBIT

car = RINGBIT(pin1, pin2)

while True:

    line_value = int(car.get_tracking())

    if line_value == 10:   # 왼쪽 검정색 10ln
        car.set_motors_speed(0, 30)
    if line_value == 1:  # 오른쪽 검정색 01
        car.set_motors_speed(30, 0)
    if line_value == 11:   # 모두 검정색 11
        car.set_motors_speed(30, 30)
    if line_value == 0:    # 모두 하얀색 00
        car.set_motors_speed(0, 0)
