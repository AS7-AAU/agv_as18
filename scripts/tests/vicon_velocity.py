#!/usr/bin/env python
import rospy as rp
from agv_as18.msg import Motor
from geometry_msgs.msg import Transform
from math import sqrt, sin, cos, atan2

robot = [0.0,0.0,0.0]
last_robot = list(robot)
R = 2
L = 12.5

def cb(data):
    global robot
    robot[0] = data.translation.x
    robot[1] = data.translation.y
    robot[2] = data.rotation.z

rp.init_node('vicon_vel')
rp.Subscriber('local_pos_ref', Transform, cb)
rp.wait_for_message('local_pos_ref', Transform) # blocks until a message is received (here to make sure we have pose feedback)
pub = rp.Publisher('vicon_velocity', Motor, queue_size=1)
r = rp.Rate(100)
while not rp.is_shutdown():
    disp = sqrt((robot[0]-last_robot[0])**2 + (robot[1]-last_robot[1])**2)
    v = disp/0.01

    angle_diff = robot[2]-last_robot[2]
    angle_diff = atan2(sin(angle_diff), cos(angle_diff))
    omega = angle_diff/0.01

    omega_A = (2*v + omega * L)/(2*R)
    omega_B = (2*v - omega * L)/(2*R)

    last_robot = list(robot)

    msg = Motor()
    msg.a = omega_A
    msg.b = omega_B
    pub.publish(msg)

    r.sleep()