#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform, TransformStamped
from tf.transformations import euler_from_quaternion
from math import degrees

is_set = False
ref = Transform()

def cb(data):
	global is_set
	global ref
	if not is_set:
	    ref = data.transform
	    is_set = True
	else:
	    msg = Transform()
	    msg.translation.x = round(data.transform.translation.x - ref.translation.x, 2)
	    msg.translation.y = round(data.transform.translation.y - ref.translation.y, 2)
	    msg.translation.z = round(data.transform.translation.z - ref.translation.z, 2)
	    msg.rotation.x = round(data.transform.rotation.x - ref.rotation.x,1)
	    msg.rotation.y = round(data.transform.rotation.y - ref.rotation.y,1)
	    msg.rotation.z = round(data.transform.rotation.z - ref.rotation.z,1)
	    msg.rotation.w = round(data.transform.rotation.w - ref.rotation.w,1)
	    pub.publish(msg)
	    
	    quat = (msg.rotation.x,msg.rotation.y,msg.rotation.z,msg.rotation.w)
      eul = euler_from_quaternion(quat)
	    eul = list(eul)
	    eul[0] = degrees(eul[0])
	    eul[1] = degrees(eul[1])
	    eul[2] = degrees(eul[2])
      rp.loginfo(eul)

rp.init_node('vicon_test')
rp.Subscriber('vicon/AS1/AS1', TransformStamped, cb)
pub = rp.Publisher('local_pos_ref', Transform, queue_size=1)
rp.spin()
