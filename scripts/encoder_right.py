#!/usr/bin/env python
from RPi import GPIO
from time import time
from math import pi
import rospy as rp
from std_msgs.msg import Float32

clk = 12
dt = 5
counter = 0
trav = 0.0
omega=0.0
last_omega=omega
rate = 1.0/200.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

rp.init_node('encoder_right')
pub = rp.Publisher('encoder_signal_right', Float32, queue_size=1)

clkLastState = GPIO.input(clk)
ta = time()
while not rp.is_shutdown():
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    elapsed = time() - ta
    if elapsed < rate:
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1
    else:
        rad = (counter/900.0)*2*pi
        omega = rad/elapsed
        ta = time()
        # trav += counter*0.01395
        print(omega)
        counter = 0
        pub.publish(omega)
            
    clkLastState = clkState

GPIO.cleanup([5,12])