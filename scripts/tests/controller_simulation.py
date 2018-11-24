#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from agv_as18.msg import Reference
from math import pi, sin, cos
import rosbag

v=0.0
omega=0.0
L = 0.17 # distance between two wheels
R = 0.04 # radius of wheel
dt = 0.01
beast = [5,5,pi/2]

def ref_cb(data):
  global v
  global omega
  v = data.v
  omega = data.omega

rp.init_node('controller_simulation')
rp.Subscriber('control_reference', Reference, ref_cb)
pub = rp.Publisher('local_pos_ref', Transform, queue_size=1)
#pub = rp.Publisher('', , queue_size=1)

bag = rosbag.Bag('beast2.bag', 'w')

r = rp.Rate(1/dt)
while not rp.is_shutdown():
  # move this to controller
  omega_A = (2*v + omega * L)/(2*R)
  omega_B = (2*v - omega * L)/(2*R)

  global beast
  beast[2] += omega*dt
  beast[0] += v*cos(beast[2])*dt
  beast[1] += v*sin(beast[2])*dt
  
  msg = Transform()
  msg.translation.x = beast[0]
  msg.translation.y = beast[1]
  msg.rotation.z = beast[2]
  pub.publish(msg)

  bag.write('beast', msg)

  r.sleep()
bag.close()