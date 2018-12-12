#!/usr/bin/python
import pid as PID
import time
import rospy as rp
from std_msgs.msg import Float32
from agv_as18.msg import Motor, Reference

P=0.006
I=0.0
D=0.0
freq=180.0
max_ang_vel=22.0
threshold= 0.5

omega_a=0.0
omega_b=0.0

def encoder_left(enc_left):
    global controller_left
    controller_left.update(enc_left.data)

def encoder_right(enc_right):
    global controller_right
    controller_right.update(enc_right.data)

def cmd_vel_cb(data):
    global controller_left
    global controller_right
    # global omega_a
    # global omega_b
    # omega_a=data.v
    # omega_b=data.omega
    controller_left.SetPoint = data.omega
    controller_right.SetPoint = data.v

def saturate(signal, setpoint):
	if signal > max_ang_vel:
		return max_ang_vel
	elif signal < -max_ang_vel:
		return -max_ang_vel
    elif signal > -threshold and signal < threshold and setpoint == 0:
        return 0.0
    return signal

controller_left = PID.PID(P,I,D)
controller_right = PID.PID(P,I,D)

controller_left.SetPoint = 0.0
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
    omega_a += controller_right.output
    omega_b += controller_left.output
    pub.publish(saturate(omega_a,controller_right.output), saturate(omega_b,controller_left.output))
    rate.sleep()
