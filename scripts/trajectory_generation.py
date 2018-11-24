#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from agv_as18 import Reference
from math import sin, cos, pi, sqrt, atan2

beast=[0,0,0]
target=[[1,1]]
max_speed = 1

def pos_ref_cb(data):
  global beast
  beast[0] = data.translation.x # x-coordinate
  beast[1] = data.translation.y # y-coordinate
  beast[2] = data.rotation.z # heading

def waypoints_cb(data):
  global target
  target = data.list  

rp.init_node('trajectory_generation')
rp.Subscriber('local_pos_ref', Transform, pos_ref_cb)
#rp.Subscriber('', , waypoints_cb)
pub = rp.Publisher('control_reference', Reference, queue_size=1)

while not rp.is_shutdown():
  if len(target) > 0:
    P = target[0] # target
    u = [P[0]-beast[0], P[1]-beast[1]] # vector from robot to target
    u_mag = sqrt(u[0]**2 + u[1]**2) # distance to target
    phi_d = atan2(u[1], u[0]) # desired heading
    e = phi_d - beast[2] # difference between desired and current heading
    phi_e = atan2(sin(e),cos(e)) # 4-quadrant angle of e
    v = max_speed
    if u_mag <= 0.5 and u_mag > 0.01:
      v *= u_mag
    elif u_mag <= 0.01:
      v *= 0.0
      target.remove(P)

    msg = Reference(v, phi_e)
    pub.publish(msg)

    print('beast: ',beast)
    #print('P: ',P)
    #print('phi_e: ',phi_e)
    #print('v: ',v)
  else:
    pass# request new target list from task_tracking node