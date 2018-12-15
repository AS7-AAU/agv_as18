#!/usr/bin/env python
import rospy as rp
import tf
from math import degrees
from geometry_msgs.msg import Transform, TransformStamped

def cb(data):
    translation = (data.transform.translation.x, data.transform.translation.y, 0)
    rotation = (data.transform.rotation.x, data.transform.rotation.y, data.transform.rotation.z, data.transform.rotation.w)
    # br = tf.TransformBroadcaster()
    # br.sendTransform(translation,
    #                  rotation,
    #                  rp.Time.now(),
    #                  'agv',
    #                  'world')

    eul = list(tf.transformations.euler_from_quaternion(rotation))
    # rp.loginfo(degrees(eul[2]))
    msg = Transform()
    msg.translation.x = data.transform.translation.x*100
    msg.translation.y = data.transform.translation.y*100
    msg.translation.z = data.transform.translation.z*100
    msg.rotation.z = eul[2]
    pub.publish(msg)

rp.init_node('vicon_agv')
rp.Subscriber('vicon/AS1/AS1', TransformStamped, cb)
pub = rp.Publisher('local_pos_ref', Transform, queue_size=1, latch=True)
rp.spin()
