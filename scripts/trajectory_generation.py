#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from std_msgs.msg import Float32MultiArray, Bool
from math import sin, cos, pi, sqrt, atan2
import serial

MAX_ANG_VEL = 48.0
R = 2.0
L = 12.5
phi_threshold = 0.2
Kp = MAX_ANG_VEL/9.8175
max_speed = (MAX_ANG_VEL * 2.0 * R - phi_threshold * L) / 2.0

beast=[0.0,0.0,0.0]
target=[]

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def pos_ref_cb(data):
  global beast
  beast[0] = data.translation.x # x-coordinate
  beast[1] = data.translation.y # y-coordinate
  beast[2] = data.rotation.z # heading

def waypoints_cb(data):
  global target
  target = list(data.data)
  # print(target)

rp.init_node('trajectory_generation')
rp.Subscriber('local_pos_ref', Transform, pos_ref_cb)
rp.Subscriber('nodes', Float32MultiArray, waypoints_cb)
pub_target=rp.Publisher('arrived_at_target', Bool, queue_size=1)
rate = rp.Rate(100)
serial_send_command = serial.Serial("/dev/ttyACM0",250000) #TODO: match baudrate with the one in the arduino code
rp.sleep(2)

while not rp.is_shutdown():
  if len(target) > 1:
    P = [target[0], target[1]] # target
    u = [P[0]-beast[0], P[1]-beast[1]] # vector from robot to target
    u_mag = sqrt(u[0]**2 + u[1]**2) # distance to target
    phi_d = atan2(u[1], u[0]) # desired heading
    e = phi_d - beast[2] # difference between desired and current heading
    phi_e = atan2(sin(e),cos(e)) # 4-quadrant angle of e

    # if state == 1:
    #   state = 2
    # if state == 2:
    #   if abs(phi_e) <= 0.5:
    #     state = 3
    #   else:
    #     v = 0
    #     phi_e *= Kp
    # if state == 3:
    #   if abs(phi_e) <= phi_threshold:
    #     state = 4
    #   else:
    #     v = 0
    #     phi_e *= Kp * translate(abs(phi_e),phi_threshold,0.5,0.2,1.0)
    # if state == 4:
    #   if abs(phi_e) > 0.15:
    #     state = 5
    #   elif u_mag <= 35:
    #     state = 6
    #   else:
    #     v = max_speed
    # if state == 5:
    #   serial_send_command.write('0&0'.encode())
    #   state = 2
    #   rp.sleep(0.1)
    # if state == 6:
    #   v = max_speed
    #   if len(target) == 2:
    #     if u_mag > 5:
    #       v *= translate(u_mag,5,35,0.2,1.0)
    #     else u_mag <= 5:
    #       target=[]
    #       pub_target.publish(True) # request new target list from task_tracking node
    #       serial_send_command.write('0&0'.encode())
    #       state = 1
    #       rp.sleep(0.1)
    #   elif u_mag <= 5:
    #     del target[0]
    #     del target[0]
    #     serial_send_command.write('0&0'.encode())
    #     state = 1
    #     rp.sleep(0.1)


    if abs(phi_e) > phi_threshold:
      v = 0.0
      omega = phi_e * Kp * pi / abs(phi_e)
      if abs(phi_e) <= 1.0:
        omega *= translate(abs(phi_e),phi_threshold,1.0,0.2,0.8)
    else:
      v = max_speed
      omega = phi_e
      if u_mag <= 35 and u_mag > 5:
        v *= translate(u_mag,5,35,0.2,1.0)
      elif u_mag <= 5:
        v *= 0.0
        omega *= 0.0
        if len(target) == 2:
          target=[]
          pub_target.publish(True) # request new target list from task_tracking node
        else:
          del target[0]
          del target[0]
    
    omega_A = (2*v + omega * L)/(2*R)
    omega_B = (2*v - omega * L)/(2*R)
    command = str(omega_A)+'&'+str(omega_B)
    print(command)
    serial_send_command.write(command.encode()) # format is:  desired speed on motor A & desired speed on motor B
  rate.sleep()