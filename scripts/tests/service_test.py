#!/usr/bin/env python
import rospy as rp
from agv_as18.srv import *

rp.wait_for_service('components')
sp = rp.ServiceProxy('components', Components)
try:
  req = ComponentsRequest()
  req.write = 1
  req.buffer = [1,0,0,0,1,1]
  req.agv_slots = ['C2','C4']
  resp = sp(req)
  print(resp)

  req = ComponentsRequest()
  req.write = 1
  req.buffer = [1,0,0,0,0,0]
  req.agv_slots = ['C2','']
  resp = sp(req)
  print(resp)
except rp.ServiceException(e):
  print(e)

try:
  #req = ComponentsRequest()
  #req.write = 0
  #resp = sp(req)
  print(sp(ComponentsRequest()))
except rp.ServiceException(e):
  print(e)
