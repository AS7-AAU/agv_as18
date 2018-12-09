#!/usr/bin/env python
import rospy as rp
from agv_as18.srv import Components, ComponentsRequest, ComponentsResponse

buffer=[0,0,0,0,0,0]

def server_cb(req):
  global buffer
  if req.write:
    buffer = req.buffer
    print(buffer)
  return ComponentsResponse(buffer)

rp.init_node('component_tracking_server')
s = rp.Service('components', Components, server_cb)
rp.spin()