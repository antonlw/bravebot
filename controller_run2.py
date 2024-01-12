from picar import front_wheels
from picar import back_wheels
import picar

from approxeng.input.selectbinder import ControllerResource

import random
import time

# change joystick left x to a turning angle 
def ax2angle(x):
    amax=135
    amin=45
    return (x+1)/2*90+amin
    


# change joystick right y to a speed value
def ax2speed(y):
    smax=100
    smin=0
    if int(y) > 0:
        print("Y is " + str(y))
    return y*100

def show_readiness()
    fw.turn(60)
    fw.turn(120)


picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

running=0

while True:
    # Get a joystick
    with ControllerResource() as joystick:
        # Loop until we're disconnected
        while joystick.connected:
            if running == 0:
                while True:
                    if presses['start']:
                        print('START pressed, getting ready')
                        show_readiness()
                        running = 1
                        break
            else:
                if presses['circle']:
                    print('CIRCLE pressed since last check')
                    print('Exit Mission.')
                    bw.stop()
                    running=0
                    break
            
            # read left x for turning angles
            fw.turn(ax2angle(joystick.lx))
            # read right y for running speed
            speed=int(ax2speed(joystick.ry))
            
            if speed>0:
                bw.speed = speed
                bw.forward()
            elif speed<0:
                bw.speed = 0-speed
                bw.backward()
            elif speed=0:
                bw.stop()
                
            # This is an instance of approxeng.input.ButtonPresses
            presses = joystick.check_presses()
            #if presses['circle']:
            #    print('CIRCLE pressed since last check')
            # We can also use attributes directly, and get at the presses object from the controller:
            #if joystick.presses.circle:
            #    print('CIRCLE pressed since last check')
            #    print('Exit Mission.')
                
            # Or we can use the 'x in y' syntax:
            #if 'triangle' in presses:
            #    print('TRIANGLE pressed since last check')
    
            # If we had any presses, print the list of pressed buttons by standard name
            #if joystick.has_presses:
            #    print(joystick.presses)

