#!/usr/bin/env python
import time
import rospy as rp
from std_msgs.msg import Int32
import sys
import select

def cb(data):
    print ("You have five seconds to answer!")

    i, o, e = select.select( [sys.stdin], [], [], 5 )

    if i:
        print ("You said", sys.stdin.readline().strip())
        pub.publish(data)
    else:
        print ("Quality control passed!")

rp.init_node('quality_check')
pub = rp.Publisher('qc',Int32,queue_size=1)
rp.Subscriber('product_assembled',Int32,cb)
rp.spin()