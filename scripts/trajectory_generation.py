#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from math import sqrt, pi, atan, atan2

beast=[0,0,pi/2]
target=[[1,1]]

def pos_ref_cb(data):
  global beast
  beast[0] = data.translation.x # x-coordinate
  beast[1] = data.translation.y # y-coordinate
  #beast[2] = data. # heading

def waypoints_cb(data):
  global target
  target = data.list  

rp.init_node('trajectory_generation')
rp.Subscriber('local_pos_ref', Transform, pos_ref_cb)
#rp.Subscriber('', , waypoints_cb)
#pub = rp.Publisher('', , queue_size=1)

while not rp.is_shutdown():
  if len(target) > 0:
    P = target[0]
    u = [P[0]-beast[0], P[1]-beast[1]]
    phi_d = atan2(u[1], u[0])
    print(phi_d)
    print(atan(u[1], u[0]))
    print('******')