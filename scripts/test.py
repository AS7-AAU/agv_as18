#!/usr/bin/env python
import rospy as rp
from agv_as18.msg import Motor as motor
from geometry_msgs.msg import Transform
from math import sqrt

def cb(data):
    dist = sqrt(data.translation.x**2 + data.translation.y**2)
    print(dist)

    if dist < 1.0:
        msg = motor()
        msg.a = 10.0
        msg.b = 10.0
        pub.publish(msg)

rp.init_node('testnode')
rp.Subscriber('local_pos_ref', Transform, cb)
pub = rp.Publisher('motor_signal', motor, queue_size=1)
rp.spin()
