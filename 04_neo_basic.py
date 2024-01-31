# 네오픽셀 기본 명령어
from microbit import *
import neopixel

num_pixels = 3
np = neopixel.NeoPixel(pin0, num_pixels)

np.fill((255, 0, 0))
np.show()
sleep(1000)
np[0] = (0, 255, 0)
np.show()
sleep(1000)
np[1] = (0, 0, 255)
np.show()
sleep(1000)
np.clear()
