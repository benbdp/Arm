from pyax12.connection import Connection
import numpy as np

sc = Connection(port='/dev/ttyACM0', baudrate=1000000)

def servo2(pos):
    if angle < 0:
        print("illegal pos")
    elif pos > 0:
        pos = -pos
        sc.goto(2, pos, 100, True)
    elif pos == 0:
        sc.goto(2, pos, 100, True)

def servo3(pos):
    sc.goto(3, pos, 100, True)

def servo4(pos):
    if pos < 0:
        pos = abs(pos)
        sc.goto(4, pos, 100, True)
    elif pos > 0:
        pos = -pos
        sc.goto(4, pos, 100, True)
    elif pos == 0:
        sc.goto(4, pos, 100, True)

def can_move(list):
    for i in list:
        if sc.is_moving(i) == True:
            return False
    return True
def servo2pos():
    pos = sc.get_present_position(2,True)
    if pos < 0:
        pos = abs(pos)
        return pos
    elif pos > 0:
        pos = -pos
        return pos
    elif pos == 0:
        return pos

def servo3pos():
    pos = sc.get_present_position(3, True)
    return pos

def servo4pos():
    pos = sc.get_present_position(4, True)
    if pos < 0:
        pos = abs(pos)
        return pos
    elif pos > 0:
        pos = -pos
        return pos
    elif pos == 0:
        return pos


def endx(leg1,joint1,leg2,joint2,leg3,joint3):
    x = leg1*np.cos(joint1)+leg2*np.cos(joint1+joint2)+leg3*np.cos(joint1+joint2+joint3)
    return(x)

def endy(leg1,joint1,leg2,joint2,leg3,joint3):
    y = leg1*np.sin(joint1)+leg2*np.sin(joint1+joint2)+leg3*np.sin(joint1+joint2+joint3)
    y = y + 4.2 # vertical offset
    return(y)

servos = [2,3,4]

try:
    working = False
    if (sc.ping(2) == True): # test the connection
        working = True
        print("working")

    while working:
        if can_move(servos) == True:
            print("Servo2: ", servo2pos(), " Servo3: ", servo3pos(), " Servo4: ", servo4pos())
            print("x: ",endx(12.3,servo2pos(),14.8,servo3pos(),13.8,servo4pos()),"y: ",endy(12.3,servo2pos(),14.8,servo3pos(),13.8,servo4pos()))
            servonum = input("Enter servo num: ")
            servonum = int(servonum)
            angle = input("Enter angle: ")
            angle = int(angle)

            if servonum == 2:
                servo2(angle)

            elif servonum == 3:
                servo3(angle)

            elif servonum == 4:
                servo4(angle)
        else:
            print("servo moving")

except:
    print("not working")
    sc.close()
