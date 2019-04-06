import RPi.GPIO as GPIO  # 导入树莓派提供的python模块


class Control(object):

    def __init__(self):
        self.led_bcm = 26
        self.fan_bcm = 18

    def set_output(self, num=None):

        if num is None:
            num = self.led_bcm
        try:
            GPIO.setmode(GPIO.BCM)  # 设置GPIO模式，BCM模式在所有树莓派通用
            GPIO.setup(num, GPIO.OUT)  # 设置GPIO26为电流输出
        except:
            pass

    def open(self, num=None):

        if num is None:
            num = self.led_bcm

        self.set_output(num=num)

        GPIO.output(num, GPIO.HIGH)  # GPIO26 输出3.3V

    def close(self, num=None):

        if num is None:
            num = self.led_bcm

        self.set_output(num=num)

        GPIO.output(num, GPIO.LOW)  # GPIO26 输出0V
