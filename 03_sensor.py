# 온도/조도센서를 사용해 온도, 조도 표시
from microbit import *

while True:
    heat = temperature()
    light = display.read_light_level()

    if button_a.was_pressed():
        display.scroll(heat)

    elif button_b.was_pressed():
        display.scroll(light)
