# 가속도 센서
from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.CONFUSED)


'''
제스처 선택 :
shake, logo up, logo down, face up, face down,
left, right, up, down, freefall, 3g
'''


