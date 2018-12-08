#!/usr/bin/env python
import rospy as rp
from std_msgs.msg import Int32
import sys
from select import select

def cb(data):
    print ("Quality control: 5 seconds to press Enter")
    i, o, e = select([sys.stdin], [], [], 5)
    print(i)
    if i:
        #print ("You said", sys.stdin.readline().strip())
        print('Defective product!')
        pub.publish(data)
    else:
        print ("Quality control passed!")

rp.init_node('quality_check')
pub = rp.Publisher('qc',Int32,queue_size=1)
rp.Subscriber('product_assembled',Int32,cb)
rp.spin()