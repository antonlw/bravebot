from picar import front_wheels
from picar import back_wheels
import picar

from approxeng.input.selectbinder import ControllerResource

import random
import time

# change joystick left x to a turning angle 
def ax2angle(self, x):
    amax=135
    amin=45
    return (x+1)/2*90+amin
    


# change joystick right y to a speed value
def ax2speed(self, y):
    smax=100
    smin=0
    return y*100


picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45


# Get a joystick
with ControllerResource() as joystick:
    # Loop until we're disconnected
    while joystick.connected:
        # read left x for turning angles
        fw.turn(ax2angle(joystick.lx))
        # read right y for running speed
        speed=ax2speed(joystick.ry)
        if speed>=0:
            bw.speed = speed
            bw.forward()
        else:
            bw.speed = 0-speed
            bw.backward()
        # This is an instance of approxeng.input.ButtonPresses
        #presses = joystick.check_presses()
        #if presses['square']
        #    print('SQUARE pressed since last check')
        # We can also use attributes directly, and get at the presses object from the controller:
        if joystick.presses.circle:
            print('CIRCLE pressed since last check')
            print('Exit Mission.')
            bw.stop()
            break
        # Or we can use the 'x in y' syntax:
        #if 'triangle' in presses:
        #    print('TRIANGLE pressed since last check')

        # If we had any presses, print the list of pressed buttons by standard name
        #if joystick.has_presses:
        #    print(joystick.presses)