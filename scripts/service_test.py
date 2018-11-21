#!/usr/bin/env python
import rospy as rp
from agv_as18.srv import *

rp.wait_for_service('components')
sp = rp.ServiceProxy('components', Components)
try:
  req = ComponentsRequest()
  req.write = 1
  req.buffer = [1,0,0,0,1,1]
  req.agv_slots = [0,0]
  resp = sp(req)
  print(resp)
except rp.ServiceException e:
  print(e)

try:
  req = ComponentsRequest()
  req.write = 0
  resp = sp(req)
  print(resp)
except rp.ServiceException e:
  print(e)
