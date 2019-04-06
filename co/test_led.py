import RPi.GPIO as GPIO   #导入树莓派提供的python模块
import time   #导入时间包，用于控制闪烁
GPIO.setmode(GPIO.BCM)   #设置GPIO模式，BCM模式在所有数码派通用
GPIO.setup(26, GPIO.OUT)   #设置GPIO26为电流输出
while True:
    GPIO.output(26, GPIO.HIGH)   #GPIO26 输出3.3V
    time.sleep(0.05)   #程序控制流程睡眠0.05秒
    GPIO.output(26, GPIO.LOW)    #GPIO26 输出0V
    time.sleep(0.05)   #程序控制流程睡眠0.05秒