from microbit import *
from time import sleep_us
from machine import time_pulse_us

class RINGBIT(object): #링비트카 메인보드

    def __init__(self, left_wheel_pin=pin1, right_wheel_pin=pin2):
        """
        링비트카 휠 핀 설정
        :param left_wheel_pin: 왼쪽 핀
        :param right_wheel_pin: 오른쪽 핀 설정
        """
        i2c.init()
        self.__left_wheel_pin = left_wheel_pin
        self.__right_wheel_pin = right_wheel_pin
        self.__right_wheel_pin.set_analog_period(10)
        self.__left_wheel_pin.set_analog_period(10)
        self.__module_pin = pin0
        if self.__left_wheel_pin != pin1 and self.__right_wheel_pin != pin1:
            self.__module_pin = pin1
        if self.__left_wheel_pin != pin2 and self.__right_wheel_pin != pin2:
            self.__module_pin = pin2

    def set_motors_speed(self, left_wheel_speed: int, right_wheel_speed: int):
        """
        모터 속도
        :param left_wheel_speed:왼쪽 속도 -100～100
        :param right_wheel_speed: 오른쪽 속도 -100～100
        :return: none
        """
        if left_wheel_speed > 100 or left_wheel_speed < -100:
            raise ValueError('speed error,-100~100')
        if right_wheel_speed > 100 or right_wheel_speed < -100:
            raise ValueError('select motor error,1,2,3,4')
        if left_wheel_speed > 0:
            left_wheel_speed = ((left_wheel_speed - 0) *
                                (256 - 153.6)) / (100 - 0) + 153.6
            self.__left_wheel_pin.write_analog(left_wheel_speed)
        elif left_wheel_speed < 0:
            left_wheel_speed = ((left_wheel_speed - 0) *
                                (51.2 - 153.6)) / (-100 - 0) + 153.6
            self.__left_wheel_pin.write_analog(left_wheel_speed)
        else:
            self.__left_wheel_pin.write_analog(153.6)

        right_wheel_speed = right_wheel_speed * -1
        if right_wheel_speed > 0:
            right_wheel_speed = ((right_wheel_speed - 0)
                                 * (256 - 153.6)) / (100 - 0) + 153.6
            self.__right_wheel_pin.write_analog(right_wheel_speed)
        elif right_wheel_speed < 0:
            right_wheel_speed = ((right_wheel_speed - 0)
                                 * (51.2 - 153.6)) / (-100 - 0) + 153.6
            self.__right_wheel_pin.write_analog(right_wheel_speed)
        else:
            self.__right_wheel_pin.write_analog(153.6)

    def get_distance(self, unit: int = 0):
        """
        초음파 거리
        :param unit:단위 0 cm 1 ft
        :return:거리
        """
        self.__module_pin.read_digital()
        self.__module_pin.write_digital(1)
        sleep_us(10)
        self.__module_pin.write_digital(0)
        ts = time_pulse_us(self.__module_pin, 1, 25000)

        distance = ts * 9 / 6 / 58
        if unit == 0:
            return distance
        elif unit == 1:
            return distance / 254

    def get_tracking(self):
        """
         라인트레이싱
        :return:00 모두 흰색
                10 왼쪽 검정색, 오른쪽 흭색
                01 왼쪽 흰색, 오른쪽 검정색
                11 모두 검정색
        """
        val = self.__module_pin.read_analog()
        if val < 150:
            return 11
        elif 150 <= val < 235:
            return 10
        elif 235 <= val < 300:
            return 1
        elif 300 <= val < 600:
            return 0
        else:
            print("Unknown ERROR")

