#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:37:40 2017

@author: willdoyle
"""

import numpy as np

import Pynamixel

hardware = Pynamixel.hardwares.USB2AX("/dev/ttyACM0", 1000000)
system = Pynamixel.System(Pynamixel.Bus(hardware))
servo1 = system.add_device(Pynamixel.devices.AX12, 1)
servo2 = system.add_device(Pynamixel.devices.AX12, 2)
servo3 = system.add_device(Pynamixel.devices.AX12, 3)

position = servo1.present_position;
servo1.moving_speed.write(0x3ff);
servo2.moving_speed.write(0x3ff);
servo3.moving_speed.write(0x3ff);
working = True;
#position = 0
while(working):
    
    direction = raw_input('Enter Direction, Up is w, Down is s, stop is q, quit is anything else:')
    print(direction)
    
    if(direction == "w"):
        servo1.goal_position.write(0x3ff)
    elif(direction == "s"):
        servo1.goal_position.write(0x000)
    elif(direction == "q"):
        servo1.goal_position.write(servo1.present_position.read())
    else:
        working = False;
        
        
        
        
print('Done running the arm')
    