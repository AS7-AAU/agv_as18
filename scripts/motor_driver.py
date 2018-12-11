#!/usr/bin/env python
import RPi.GPIO as gpio
import rospy as rp
from agv_as18.msg import Motor

max_ang_vel = 25

pins = {
    'AIN1' : 17,
    'AIN2' : 24,
    'BIN1' : 4,
    'BIN2' : 18,
    'PWMA' : 23,
    'PWMB' : 27,
    'STBY' : 22
}

gpio.setmode(gpio.BCM)
for key in pins.keys():
    gpio.setup(pins[key], gpio.OUT)

gpio.output(pins['STBY'], gpio.HIGH) #disable stby

pwm_a = gpio.PWM(pins['PWMA'], 1000)
pwm_b = gpio.PWM(pins['PWMB'], 1000)

pwm_a.start(0)
pwm_b.start(0)

def motor_signal_cb(data):
    if data.a >= 0:
        gpio.output(pins['AIN1'], gpio.HIGH)
        gpio.output(pins['AIN2'], gpio.LOW)
    else:
        gpio.output(pins['AIN1'], gpio.LOW)
        gpio.output(pins['AIN2'], gpio.HIGH)
    if data.b >= 0:
        gpio.output(pins['BIN1'], gpio.LOW)
        gpio.output(pins['BIN2'], gpio.HIGH)
    else:
        gpio.output(pins['BIN1'], gpio.HIGH)
        gpio.output(pins['BIN2'], gpio.LOW)
    omega_a = abs(data.a) * 100.0/max_ang_vel
    omega_b = abs(data.b) * 100.0/max_ang_vel
    pwm_a.ChangeDutyCycle(omega_a)
    pwm_b.ChangeDutyCycle(omega_b)

rp.init_node('motor_driver')
rp.Subscriber('motor_signal', Motor, motor_signal_cb)
rp.spin()

for key in pins.keys():
    pwm_a.stop()
    pwm_b.stop()
    gpio.output(pins[key], gpio.LOW)
    gpio.cleanup(pins[key])

