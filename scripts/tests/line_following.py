#!/usr/bin/env python
import rospy as rp
from std_msgs.msg import Float32MultiArray, Bool

targets = [
    [100.0, 0.0]
]

# targets = [
#     [100.0, 0.0  ],
#     [100.0, 100.0],
#     [0.0,   100.0],
#     [0.0,   0.0  ]
# ]

def send_waypoints():
    # send targets one by one (stop at each target)
    global targets
    msg = Float32MultiArray()
    if len(targets) > 0:
        for el in targets[0]:
            msg.data.append(el)
        del targets[0]
        waypoint_pub.publish(msg)

    # send every target at once (only stops at last one)
    # rp.sleep(2.0)
    # global targets
    # msg = Float32MultiArray()
    # if len(targets) > 0:
    #     for i in range(len(targets)):
    #         for el in targets[i]:
    #             msg.data.append(el)
    #     waypoint_pub.publish(msg)

def new_target(data):
    send_waypoints()

rp.init_node('line_following_test')
rp.Subscriber('arrived_at_target', Bool, new_target)
waypoint_pub = rp.Publisher('nodes', Float32MultiArray, queue_size=1, latch=True)
send_waypoints()

rp.spin()
