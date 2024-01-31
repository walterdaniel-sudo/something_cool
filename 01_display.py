from microbit import *

name = "Hello!"
emoticon = Image.SURPRISED\

while True:
    if button_a.was_pressed():
        display.show(name)
    elif button_b.was_pressed():
        display.show(emoticon)

'''
감정 이모티콘
HAPPY, HEART, HEART_SMALL, SMILE, SAD, CONFUSED,
ANGRY, ASLEEP, SURPRISED, SILLY, FABULOUS, MEH,
YES, NO
'''
