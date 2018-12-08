#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform, TransformStamped
import tf
from math import degrees

is_set = False
ref = TransformStamped()


def cb(data):
    global is_set
    global ref
    if not is_set:
        ref = data
        is_set = True
    else:
        # msg = TransformStamped()
        # msg.translation.x = round(
        #     data.transform.translation.x - ref.translation.x, 2)*100
        # msg.translation.y = round(
        #     data.transform.translation.y - ref.translation.y, 2)*100
        # msg.translation.z = round(
        #     data.transform.translation.z - ref.translation.z, 2)*100
        #msg.rotation.x = round(data.transform.rotation.x - ref.rotation.x, 1)
        #msg.rotation.y = round(data.transform.rotation.y - ref.rotation.y, 1)
        #msg.rotation.z = round(data.transform.rotation.z - ref.rotation.z, 1)
        #msg.rotation.w = round(data.transform.rotation.w - ref.rotation.w, 1)
        
        # pub.publish(msg)


        # br = tf.TransformBroadcaster()
        # br.sendTransform((msg.translation.x/100, msg.translation.y/100, 0), (msg.rotation.x,
                                                                            #  msg.rotation.y, msg.rotation.z, msg.rotation.w), rp.Time.now(), 'agv', 'world')

        #quat = (msg.rotation.x, msg.rotation.y, msg.rotation.z, msg.rotation.w)
        pass
    eul = list(tf.transformations.euler_from_quaternion((data.transform.rotation.x, data.transform.rotation.y, data.transform.rotation.z, data.transform.rotation.w)))
    eul[0] = degrees(eul[0])
    eul[1] = degrees(eul[1])
    eul[2] = degrees(eul[2])
    # rp.loginfo(eul)
    # rp.loginfo(data.transform.translation)

    msg = Transform()
    msg.translation = data.transform.translation
    msg.rotation.z = eul[2]
    print(msg)


rp.init_node('vicon_test')
rp.Subscriber('vicon/AS1/AS1', TransformStamped, cb)
pub = rp.Publisher('local_pos_ref', Transform, queue_size=1)
rp.spin()
