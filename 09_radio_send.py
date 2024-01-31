# 송신
from microbit import *
import radio

radio.config(group = 1)
radio.on()

while True:
    if button_a.is_pressed():
        radio.send('1')
        display.show('1')
    if button_b.is_pressed():
        radio.send('2')
        display.show('2')

