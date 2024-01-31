# 네오픽셀 함수 만들기
from microbit import *
import neopixel

num_pixels = 3
np = neopixel.NeoPixel(pin0, num_pixels)

def set_color(red, green, blue):
    for i in range(num_pixels):
        np[i] = (red, green, blue)
    np.show()

while True:
    set_color(255, 0, 0)
    sleep(1000)
    set_color(0, 255, 0)
    sleep(1000)
    set_color(0, 0, 255)
    sleep(1000)
