#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Float32
import math

Left_RotateAPin = 13 # Define as CLK Pin
Left_RotateBPin = 6 # Define as DT Pin

Permiter = 0.028
globalCounter = 0
flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup([Left_RotateAPin,Left_RotateBPin], GPIO.IN)

def rotaryDeal():
	global flag
	global Last_RoB_Status
	global Current_RoB_Status
	global globalCounter

	Last_RoB_Status = GPIO.input(Left_RotateBPin)

	while (not GPIO.input(Left_RotateAPin)):
		Current_RoB_Status = GPIO.input(Left_RotateBPin)
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
		if time.time() - timer_a >0.0052:
			timer_a = time.time()
			enc_a = (globalCounter * 74.2837) # Encoder value in RPM
			enc_a = enc_a * (2*math.pi/60) # Encoder value in angular velocity per sec	
			globalCounter =0

			print("Encoder left value", enc_a)
			pub.publish(enc_a)

def destroy():
	GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
	setup()
	pub = rospy.Publisher('encoder_signal_left', Float32, queue_size = 1)
    rospy.init_node('encoder_left')

	try:
		encoder_signal_cb()
	except rospy.ROSInterruptException: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
		destroy()
