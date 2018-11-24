#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from agv_as18 import Reference
from math import pi, sin, cos

v=0.0
omega=0.0
L = 0.17 # distance between two wheels
R = 0.04 # radius of wheel
dt = 0.01
beast = [0,0,0]

def ref_cb(data):
  global v
  global omega
  v = data.v
  omega = data.omega

rp.init_node('controller_simulation')
rp.Subscriber('control_reference', Reference, ref_cb)
pub = rp.Publisher('local_pos_ref', Transform, queue_size=1)
#pub = rp.Publisher('', , queue_size=1)

r = rp.Rate(1/dt)
while not rp.is_shutdown():
  # move this to controller
  omega_A = (2*v + omega * L)/(2*R)
  omega_B = (2*v - omega * L)/(2*R)

  global beast
  beast[0] += v*cos(omega)*dt
  beast[1] += v*sin(omega)*dt
  beast[2] += omega*dt
  
  msg = Transform()
  msg.translation.x = beast[0]
  msg.translation.y = beast[1]
  msg.rotation.z = beast[2]
  pub.publish(msg)

  r.sleep()