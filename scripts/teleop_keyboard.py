#!/usr/bin/env python
import rospy
import serial
import sys, select, termios, tty

max_ang_vel = 48.0

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
        'i':(max_ang_vel,max_ang_vel),
        'o':(max_ang_vel/2,max_ang_vel),
        'j':(max_ang_vel,-max_ang_vel),
        'l':(-max_ang_vel,max_ang_vel),
        'u':(max_ang_vel,max_ang_vel/2),
        ',':(-max_ang_vel,-max_ang_vel),
        '.':(-max_ang_vel,-max_ang_vel),
        'm':(-max_ang_vel,-max_ang_vel),
    }

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('teleop_keyboard')
    serial_send_command = serial.Serial("/dev/ttyACM0",250000) #TODO: match baudrate with the one in the arduino code
    rospy.sleep(2)

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

            command = str(a)+'&'+str(b)
            serial_send_command.write(command.encode()) # format is:  desired speed on motor A & desired speed on motor B

    except Exception as e:
        print(e)

    finally:
        serial_send_command.write('0.0&0.0'.encode()) # format is:  desired speed on motor A & desired speed on motor B
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
