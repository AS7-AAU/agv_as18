#!/usr/bin/python
import pid as PID
import time
import rospy as rp
from std_msgs.msg import Float32
from agv_as18.msg import Motor, Reference

P=1.0
I=0.0
D=0.0
freq=100.0

def encoder_left(enc_left):
    global controller_left
    controller_left.update(enc_left.data)

def encoder_right(enc_right):
    global controller_right
    controller_right.update(enc_right.data)

def cmd_vel_cb(data):
    global controller_left
    global controller_right
    controller_left.SetPoint = data.omega
    controller_right.SetPoint = data.v

def saturate(signal):
	if signal > 54:
		return 54
	elif signal < -54:
		return -54
	return signal

rp.init_node("pid")
rp.Subscriber("encoder_signal_left", Float32, encoder_left)	
rp.Subscriber("encoder_signal_right", Float32, encoder_right)
rp.Subscriber("cmd_vel", Reference, cmd_vel_cb)
pub = rp.Publisher("motor_signal", Motor, queue_size=1)
rate = rp.Rate(freq)

controller_left = PID.PID(P,I,D)
controller_right = PID.PID(P,I,D)

controller_left.SetPoint = 0.0
controller_left.setSampleTime(1.0/freq)
controller_right.SetPoint = 0.0
controller_right.setSampleTime(1.0/freq)

while not rp.is_shutdown():
    pub.publish(saturate(controller_right.output), saturate(controller_left.output))
    rate.sleep()