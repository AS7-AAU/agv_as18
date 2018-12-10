#!/usr/bin/env python
import rospy as rp
from geometry_msgs.msg import Transform, TransformStamped
from agv_as18.msg import Reference
from math import pi, sin, cos
import rosbag
import tf

v=0.0
omega=0.0
L = 12.5 # distance between two wheels
R = 2 # radius of wheel
dt = 0.01
beast = [0.0,0.0,-pi/2]

def ref_cb(data):
  global v
  global omega
  v = data.v
  omega = data.omega

rp.init_node('controller_simulation')
rp.Subscriber('control_reference', Reference, ref_cb)
pub = rp.Publisher('local_pos_ref', Transform, queue_size=1)

# bag = rosbag.Bag('beast3.bag', 'w')

r = rp.Rate(1/dt)
while not rp.is_shutdown():
  # move this to controller
  omega_A = (2*v + omega * L)/(2*R)
  omega_B = (2*v - omega * L)/(2*R)

  global beast
  beast[2] += omega*dt
  beast[0] += v*cos(beast[2])*dt
  beast[1] += v*sin(beast[2])*dt
  
  msg = Transform()
  msg.translation.x = beast[0]
  msg.translation.y = beast[1]
  msg.rotation.z = beast[2]+pi/2
  pub.publish(msg)

  br = tf.TransformBroadcaster()
  br.sendTransform((beast[0]/100,beast[1]/100,0),
                    tf.transformations.quaternion_from_euler(0,0,beast[2]),
                    rp.Time.now(),
                    'agv',
                    'world')

  # bag.write('beast', msg)

  r.sleep()
# bag.close()