#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform
from agv_as18.msg import Waypoints, Task
from agv_as18.srv import *

#locations
BEAST = ['BEAST',70.0,220.0]
""" AS = ['AS',170.0,125.0]
C1 = ['C1',5.0,200.0]
C2 = ['C2',5.0,170.0]
C3 = ['C3',5.0,140.0]
C4 = ['C4',5.0,110.0]
C5 = ['C5',5.0,80.0]
C6 = ['C6',5.0,50.0]
MWP1 = ['MWP1',52.5,222.5]
MWP2 = ['MWP2',52.5,125.0]
MWP3 = ['MWP3',52.5,27.7] """

task_sequence=[]
b=[]
buffer=[]
agv_slots=[]

def pos_cb(data):
  BEAST[1]=data.translation.x
  BEAST[2]=data.translation.y

def waypoints_cb(data):
  global task_sequence
  global b
  task_sequence = []
  b = []

  b = data.b
  for task in data.task_seq:
    el = []
    el.append(task.name)
    el.append(task.x)
    el.append(task.y)
    task_sequence.append(el)

def fetch_cloud():
  try:
    resp = sp(ComponentsRequest())
    return resp.buffer, resp.agv_slots
  except rp.ServiceException(e):
    print(e)

def set_cloud(buffer, agv_slots):
  try:
    sp(ComponentsRequest(1, [1], ['C1']))
  except rp.ServiceException(e):
    print(e)

rp.init_node('task_tracking')
rp.Subscriber('local_pos_ref', Transform, pos_cb)
rp.Subscriber('waypoints', Waypoints, waypoints_cb)
#waypoint_pub = rp.Publisher('', , queue_size=1)
rp.wait_for_service('components')
sp = rp.ServiceProxy('components', Components)

set_cloud([1,0,0,0,1,1], ['C2', 'C2'])
buffer, agv_slots = fetch_cloud()

rp.spin()
