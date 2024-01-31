# 수신: 원격제어 자동차
from microbit import *
from Ringbit import RINGBIT
import radio

car = RINGBIT(pin1, pin2)

radio.config(group=9)
radio.on()

while True:
    message = radio.receive()
    if message == '1':        # 좌회전
        car.set_motors_speed(0, 50)
    elif message == '2':      # 우회전
        car.set_motors_speed(50, 0)
    elif message == '3':      # 직진
        car.set_motors_speed(100, 100)
    elif message == '4':      # 후진
        car.set_motors_speed(-100, -100)
    elif message == '5':      # 정지
        car.set_motors_speed(0, 0)
