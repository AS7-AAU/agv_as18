#!/usr/bin/python
import pid as PID
import time
import rospy as rp
from std_msgs.msg import Float32
from agv_as18.msg import Motor, Reference

P=7.0
I=0.0
D=0.1
freq=180.0
max_ang_vel=25.0

omega_a=0.0
omega_b=0.0

def encoder_left(enc_left):
    global controller_left
    global omega_b
    controller_left.update(enc_left.data)
    omega_b=enc_left.data

def encoder_right(enc_right):
    global controller_right
    global omega_a
    controller_right.update(enc_right.data)
    omega_a=enc_right.data

def cmd_vel_cb(data):
    global controller_left
    global controller_right
    controller_left.SetPoint = data.omega
    controller_right.SetPoint = data.v

def saturate(signal):
	if signal > max_ang_vel:
		return max_ang_vel
	elif signal < -max_ang_vel:
		return -max_ang_vel
	return signal

controller_left = PID.PID(P,I,D)
controller_right = PID.PID(P,I,D)

controller_left.SetPoint = 20.0
controller_left.setSampleTime(1.0/freq)
controller_right.SetPoint = 0.0
controller_right.setSampleTime(1.0/freq)

rp.init_node("pid")
rp.Subscriber("encoder_signal_left", Float32, encoder_left)	
rp.Subscriber("encoder_signal_right", Float32, encoder_right)
rp.Subscriber("cmd_vel", Reference, cmd_vel_cb)
pub = rp.Publisher("motor_signal", Motor, queue_size=1)
rate = rp.Rate(freq)


while not rp.is_shutdown():
    #pub.publish(saturate(controller_right.output), saturate(controller_left.output))
    pub.publish(saturate(omega_a), saturate(omega_b))
    rate.sleep()
