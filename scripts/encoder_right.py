#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Float32
import math

Right_RotateAPin = 12  # Define as CLK Pin
Right_RotateBPin = 5  # Define as DT Pin

Permiter = 0.028
globalCounter = 0
flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([Right_RotateAPin, Right_RotateBPin], GPIO.IN)

def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter

    Last_RoB_Status = GPIO.input(Right_RotateBPin)

    while (not GPIO.input(Right_RotateAPin)):
        Current_RoB_Status = GPIO.input(Right_RotateBPin)
        flag = 1
    if flag == 1:
        flag = 0
        if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter = globalCounter + 1
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter = globalCounter - 1

def btnISR(channel):
    global globalCounter
    globalCounter = 0

def encoder_signal_cb():
    global globalCounter
    timer_a = time.time()

    while not rospy.is_shutdown():
        rotaryDeal()
        if time.time() - timer_a > 0.0052:
            timer_a = time.time()
            # Encoder value calculated from test
            enc_b = (globalCounter * 74.2837)
            enc_b = enc_b * (2*math.pi/60)  # Encoder value as angular velocity
            globalCounter = 0
            
            print("Encoder value right = ", enc_b)
            pub.publish(enc_b)

def destroy():
    GPIO.cleanup()  # Release resource

if __name__ == '__main__':  # Program start from here
    setup()
    pub = rospy.Publisher('encoder_signal_right', Float32, queue_size=1)
    rospy.init_node('encoder_right')

    try:
        encoder_signal_cb()
    # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
    except rospy.ROSInterruptException:
        destroy()
