#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:37:40 2017

@author: willdoyle
"""

import numpy as np
from pyax12.connection import Connection

sc = Connection(port = '/dev/ttyACM0', baudrate = 1000000)


def read_single_keypress():
    """Waits for a single keypress on stdin.

    This is a silly function to call if you need to do it a lot because it has
    to store stdin's current setup, setup stdin for reading single keystrokes
    then read the single keystroke then revert stdin back after reading the
    keystroke.

    Returns the character of the key that was pressed (zero on
    KeyboardInterrupt which can happen when a signal gets handled)

    """
    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK 
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR 
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
    # read a single keystroke
    try:
        ret = sys.stdin.read(1) # returns a single character
    except KeyboardInterrupt: 
        ret = 0
    finally:
        # restore old state
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
    return ret

def moveAnyServo(num,pos):
    sc.goto(num, pos, 70, True)
    
#method for moving the joints with *some safety*. range is between 0 and 1023, so this will save
#us going over
def smartMove(num, pos):
    if(num == 4):
        if(pos < 150 and pos > -150):
            sc.goto(4, pos, 70, True)
    if(num == 3):
        if(pos < 150 and pos > -150):
            sc.goto(3, pos, 50, True)
            
    if(num == 2):
        if(pos < 150 and pos > -150):
            sc.goto(2, pos, 30, True)
            
#little thing to decide the 'diff' in main for smartmove. this sets the interval to move to every keypress
#reading. they are different values because some joints are too jerky/slow if you use one number
def optimalPosDiff(servonum):
    if(servonum == 4):
        return -13;
    if(servonum == 3):
        return 10;
    if(servonum == 2):
        return 8;


def getAngleOne():
    angleOne = sc.get_present_position(2, True)
    return angleOne

def getAngleTwo():
    angleTwo = sc.get_present_position(3, True)
    return angleTwo

def getAngleThree():
    angleThree = sc.get_present_position(4, True)
    return angleThree




if __name__ == "__main__":
    servo_num = 4
    while True:
        key = read_single_keypress()
        #plus and minus vary between servos!!!! right now I'll fix it to work for 4
        if key == 'q':
            break
        if key == 'w':
            smartMove(servo_num, sc.get_present_position(servo_num, True) + optimalPosDiff(servo_num))
        if key == 's':
            smartMove(servo_num, sc.get_present_position(servo_num, True) - optimalPosDiff(servo_num))
        if key == '2':
            servo_num = 2;
        if key == '3':
            servo_num = 3;
        if key == '4':
            servo_num = 4;
        if key == 't':
            sc.goto(4, 0, 70, True)
        if key == 'r':
            print('Servo: ', servo_num, 'Position:', sc.get_present_position(servo_num, True))
        print('Servo: ', servo_num, 'Position:', sc.get_present_position(servo_num, True))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

