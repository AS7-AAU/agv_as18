#!/usr/bin/env python
import rospy
from agv_as18.msg import Motor as motor

import sys, select, termios, tty

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
anything else : stop
CTRL-C to quit
"""

moveBindings = {
        'i':(10,10),
        'o':(5,10),
        'j':(10,-10),
        'l':(-10,10),
        'u':(10,5),
        ',':(-10,-10),
        '.':(-5,-10),
        'm':(-10,-5),
    }

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    pub = rospy.Publisher('motor_signal', motor, queue_size = 1)
    rospy.init_node('teleop_keyboard')

    a = 0.0
    b = 0.0

    try:
        print(msg)
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                a = moveBindings[key][0]
                b = moveBindings[key][1]
            else:
                a = 0.0
                b = 0.0
                if (key == '\x03'):
                    break

            msg = motor()
            msg.a = a
            msg.b = b
            pub.publish(msg)

    except Exception as e:
        print(e)

    finally:
        msg = motor()
        msg.a = 0.0
        msg.b = 0.0
        pub.publish(msg)

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
