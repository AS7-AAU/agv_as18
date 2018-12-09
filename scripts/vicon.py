#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform, TransformStamped
import tf
from math import degrees

def cb(data):
    translation = (data.transform.translation.x/100, data.transform.translation.y/100, 0)
    rotation = (data.transform.rotation.x, data.transform.rotation.y, data.transform.rotation.z, data.transform.rotation.w)
    # br = tf.TransformBroadcaster()
    # br.sendTransform(translation,
                     rotation,
                     rp.Time.now(),
                     'agv',
                     'world')

    eul = list(tf.transformations.euler_from_quaternion(rotation))
    # rp.loginfo(degrees(eul[2]))
    msg = Transform()
    msg.translation = data.transform.translation
    msg.rotation.z = eul[2]

rp.init_node('vicon_test')
rp.Subscriber('vicon/AS1/AS1', TransformStamped, cb)
pub = rp.Publisher('local_pos_ref', Transform, queue_size=1)
rp.spin()
