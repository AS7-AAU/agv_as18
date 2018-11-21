#!/usr/bin/env python
import rospy as rp
from agv_as18.srv import *

buffer=[]
agv_slots=[]

def server_cb(req):
  global buffer
  global agv_slots
  if req.write:
    buffer = req.buffer
    agv_slots = req.agv_slots
  resp = ComponentsResponse()
  resp.buffer = buffer
  resp.agv_slots = agv_slots
  return resp

rp.init_node('component_tracking_server')
s = rp.Service('components', Components, server_cb)
rp.spin()