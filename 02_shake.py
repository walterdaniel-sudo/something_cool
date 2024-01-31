# 가속도 센서를 활용한 만보기
from microbit import *

num = 0

while True:
    display.show(Image.HAPPY)

    if accelerometer.is_gesture('shake'):
        num += 1
        display.show(Image.HEART)
        sleep(200)

    if button_a.was_pressed():
        display.clear()
        num = 0
        display.scroll(num)

    elif button_b.was_pressed():
        display.scroll(num)

