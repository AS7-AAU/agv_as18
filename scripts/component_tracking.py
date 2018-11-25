#!/usr/bin/env python
import rospy as rp
from agv_as18.srv import *

buffer=[]

def server_cb(req):
  global buffer
  if req.write:
    buffer = req.buffer
  resp = ComponentsResponse()
  resp.buffer = buffer
  return resp

rp.init_node('component_tracking_server')
s = rp.Service('components', Components, server_cb)
rp.spin()