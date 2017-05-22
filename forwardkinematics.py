#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 20:35:13 2017

@author: willdoyle
"""

import numpy as np

#cm
AB = 12.3
BC = 14.8
CD = 13.8
vOffset = 4.2

thetaOne = np.radians(90)
thetaTwo = np.radians(0)
thetaThree = np.radians(0)

# little method that calculates the x, y position of end effector of 3 joint arm

def calculateXY():
    
    x = AB * np.cos(thetaOne) + BC* np.cos(thetaOne + thetaTwo) + CD* np.cos(thetaOne + thetaTwo + thetaThree)
    y = AB * np.sin(thetaOne) + BC* np.sin(thetaOne + thetaTwo) + CD* np.sin(thetaOne + thetaTwo + thetaThree)
    print(x)
    print(y)
    
    
    
# method to calculate x position of end effector on 3 joint arm 
def calculateX():
    x = AB * np.cos(thetaOne) + BC* np.cos(thetaOne + thetaTwo) + CD* np.cos(thetaOne + thetaTwo + thetaThree)
    return x

#method to calculate y position of end effector on 3 joint arm
def calculateY():
    y = AB * np.sin(thetaOne) + BC* np.sin(thetaOne + thetaTwo) + CD* np.sin(thetaOne + thetaTwo + thetaThree)
    return y + vOffset
  
    





#method to solve for angle combinations for a 3 joint arm given desired x and y, and desired end effector angle RELATIVE TO THE GROUND,
#NOT TO THE END OF THE WRIST!!!!!!!
#see page 4 of this document https://ocw.mit.edu/courses/mechanical-engineering/2-12-introduction-to-robotics-fall-2005/lecture-notes/chapter4.pdf
#THESE TWO METHODS TAKE DESIRED EE LOCATIONS, NOT DESIRED WRIST ANGLES
def solveInverseKinematicSolutions(eeDesiredAngle, desiredX, desiredY):
    # figure out where the tip of wrist is. probably needs to 
  
    wristx = desiredX -  CD* np.cos(eeDesiredAngle)     
    wristy = desiredY - CD * np.sin(np.radians(eeDesiredAngle))
    
    print('Wristx:', wristx)
    print('Wristy:', wristy)
    
    shoulderAngle = solveShoulderAngle(eeDesiredAngle, desiredX, desiredY)
    
    elbowAngle = solveElbowAngle(eeDesiredAngle, desiredX, desiredY)
    
    wristAngle = solveWristAngle(eeDesiredAngle, shoulderAngle, elbowAngle)
    
    print('Shoulder Angle:', shoulderAngle)
    print('Elbow Angle:', elbowAngle)
    print('Wrist Angle:', wristAngle)
    
def solveInverseKinematicSolutionsWithVOffset(eeDesiredAngle, desiredX, desiredY):
    # figure out where the tip of wrist is. probably needs to 
    desiredY = desiredY - vOffset
    wristx = desiredX -  CD* np.cos(np.radians(eeDesiredAngle))      
    wristy = desiredY - CD * np.sin(np.radians(eeDesiredAngle))
    
    print('Wristx:', wristx)
    print('Wristy:', wristy)
    
    shoulderAngle = solveShoulderAngle(eeDesiredAngle, desiredX, desiredY)
    
    elbowAngle = solveElbowAngle(eeDesiredAngle, desiredX, desiredY)
    
    wristAngle = solveWristAngle(eeDesiredAngle, shoulderAngle, elbowAngle)
    
    print('Shoulder Angle:', shoulderAngle)
    print('Elbow Angle:', elbowAngle)
    print('Wrist Angle:', wristAngle)

def solveElbowAngle(eeDesiredAngle, desiredX, desiredY):
    #this uses the law of cosines to solve for the elbow angle
    #c^2 = a^2 + b^2 -2abcos(elbowangle), where elbowangle is opposite side c
    #c^2, from the pythagorean theorem, is just xwrist^2 + ywrist^2
   
    wristx = desiredX -  CD* np.cos(np.radians(eeDesiredAngle))      
    wristy = desiredY - CD * np.sin(np.radians(eeDesiredAngle))
    
    
    
    elbowAngle = np.arccos((np.power(AB, 2) + np.power(BC, 2) - np.power(wristx, 2) - np.power(wristy, 2))/(2 * AB * BC))
    
    #print('ELBOWANGLE:', elbowAngle)
    

    return np.degrees(elbowAngle)


def solveShoulderAngle(eeDesiredAngle, desiredX, desiredY):
    #similar process to solveElbowAngle
    
    wristx = desiredX -  CD* np.cos(np.radians(eeDesiredAngle))     
    wristy = desiredY - CD * np.sin(np.radians(eeDesiredAngle))
    
    arctanOfWrist = np.arctan(wristy/wristx)
    
    shoulderAngle = arctanOfWrist - np.arccos((np.power(wristx, 2) + np.power(wristy, 2) + np.power(AB, 2) - np.power(BC, 2))/(2 * AB * np.sqrt(np.power(wristx, 2) + np.power(wristy, 2))))
    
    shoulderAngle = np.round(np.degrees(shoulderAngle), 3)
    #print('SHOULDERANGLE:', shoulderAngle)
    #round it off so we don't get any crazy decimals to large negative exponents.
    return shoulderAngle
    


def solveWristAngle(eeDesiredAngle, shoulderAngle, elbowAngle):
    return eeDesiredAngle - shoulderAngle - elbowAngle


def solveInnerAngle(angleInDegrees):
    return 180 -angleInDegrees

def flipKinematics(shoulderAngle, elbowAngle, wristAngle, wristx, wristy, desiredEEAngle):
    #formula taken from mit article, the whole arccos thing is the inner angle between the AB length and 
    #the "hypotenuse" from the origin to the wrist
    newShoulderAngle = shoulderAngle + 2 * np.degrees(np.arccos((np.power(wristx, 2) + np.power(wristy, 2) + np.power(AB, 2) - np.power(BC, 2))/(2 * AB * np.sqrt(np.power(wristx, 2) + np.power(wristy, 2)))))
    newShoulderAngle = np.round(newShoulderAngle, 3)
    print('Flipped Shoulder Angle:', newShoulderAngle)
    
    newElbowAngle = elbowAngle * -1
    print('Flipped Elbow Angle:', newElbowAngle)
    
    newWristAngle = desiredEEAngle - newShoulderAngle - newElbowAngle
    newWristAngle = np.round(newWristAngle, 3)
    print('Flipped Wrist Angle:', newWristAngle)
    

solveInverseKinematicSolutionsWithVOffset(0, 26.1, 19)
flipKinematics(-19.87, 1.27, 18.6, 12.3, 14.8, 0)

#solveShoulderAngle(0, 32.96, 19.16)
#   solveElbowAngle(0, 32.96, 19.16)
#x   
#print(AB *np.cos(np.radians(100.541)) + BC * np.cos(np.radians(100.541 + -90.0)) + CD * np.cos(np.radians(100.541 - 90.0 - 10.541)))   
