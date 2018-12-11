#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from std_msgs.msg import Float32MultiArray, Bool
from agv_as18.msg import Reference
from math import sin, cos, pi, sqrt, atan2

beast=[0.0,0.0,-pi/2]
target=[]
max_speed = 47.75
R = 2
L = 12.5

def pos_ref_cb(data):
  global beast
  beast[0] = data.translation.x # x-coordinate
  beast[1] = data.translation.y # y-coordinate
  beast[2] = data.rotation.z-pi/2 # heading

def waypoints_cb(data):
  global target
  target = list(data.data)
  print(target)

rp.init_node('trajectory_generation')
rp.Subscriber('local_pos_ref', Transform, pos_ref_cb)
rp.Subscriber('nodes', Float32MultiArray, waypoints_cb)
pub = rp.Publisher('control_reference', Reference, queue_size=1)
pub_cmd_vel = rp.Publisher('cmd_vel', Reference, queue_size=1)
pub_target=rp.Publisher('arrived_at_target', Bool, queue_size=1)

while not rp.is_shutdown():
  #global target
  # print(target)
  if len(target) > 1:
    P = [target[0], target[1]] # target
    u = [P[0]-beast[0], P[1]-beast[1]] # vector from robot to target
    u_mag = sqrt(u[0]**2 + u[1]**2) # distance to target
    phi_d = atan2(u[1], u[0]) # desired heading
    e = phi_d - beast[2] # difference between desired and current heading
    phi_e = atan2(sin(e),cos(e)) # 4-quadrant angle of e

    if abs(phi_e) > 0.1:
      v = 0
    else:
      v = max_speed
      if len(target) == 2:
        if u_mag <= 25 and u_mag > 3:
          v *= u_mag/50
        elif u_mag <= 3:
          v *= 0.0
          phi_e *= 0.0
          target=[]
          pub_target.publish(True) # request new target list from task_tracking node
      elif u_mag <= 3:
        del target[0]
        del target[0]
    
    omega_A = (2*v + phi_e * L)/(2*R)
    omega_B = (2*v - phi_e * L)/(2*R)
    #print(v, phi_e)
    #print(omega_A, omega_B)
    pub.publish(Reference(v, phi_e))
    pub_cmd_vel.publish(Reference(omega_A, omega_B))