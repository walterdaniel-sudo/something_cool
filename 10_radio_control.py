# 송신 : 원격제어
from microbit import *
import radio

radio.config(group=9)
radio.on()

while True:
    if accelerometer.was_gesture('left'):
        radio.send('1')
        display.show('1')
    elif accelerometer.was_gesture('right'):
        radio.send('2')
        display.show('2')
    elif accelerometer.was_gesture('up'):
        radio.send('3')
        display.show('3')
    elif accelerometer.was_gesture('down'):
        radio.send('4')
        display.show('4')
    elif button_a.is_pressed():
        radio.send('5')
        display.show('5')
