from RPi import GPIO
from time import sleep, time

clk = 13
dt = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
trav = 0.0
clkLastState = GPIO.input(clk)

try:
        ta = time()
        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        rad = (counter/900.0)*6.28
                        omega = rad/(time()-ta)
                        ta = time()
                        trav += counter*0.01395
                        print omega
                        counter = 0
                clkLastState = clkState
                #sleep(0.01)
finally:
        GPIO.cleanup()
