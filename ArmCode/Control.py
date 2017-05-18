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


def endx(leg1,joint1,leg2,joint2,leg3,joint3):  # calculate the x value of the end effector
    x = (leg1*np.cos(np.deg2rad(joint1)))+(leg2*np.cos(np.deg2rad(joint1+joint2)))+(leg3*np.cos(np.deg2rad(joint1+joint2+joint3)))
    return(x)

def endy(leg1,joint1,leg2,joint2,leg3,joint3):  # calculate the y value of the end effector
    y = (leg1*np.sin(np.deg2rad(joint1)))+(leg2*np.sin(np.deg2rad(joint1+joint2)))+(leg3*np.sin(np.deg2rad(joint1+joint2+joint3)))
    y = y + 4.2  # vertical offset
    return(y)

# find wrist positions
def wristposx(tx,leg3,eo):
    eo = np.deg2rad(eo)
    if eo < (np.pi/2):
        xw = tx-leg3*(np.cos(eo))
        return xw
    else:
        xw = tx + leg3 * (np.cos(eo))
        return xw

def wristposy(ty,leg3,eo):
    eo = np.deg2rad(eo)
    yw = ty-leg3*(np.sin(eo))
    return yw


# theta one
def joint1(xw,yw,leg1,leg2):
    y = np.arccos(((xw**2) + (yw**2) + (leg1**2) - (leg2**2)) / (2 * leg1 * np.sqrt((xw**2) + (yw**2))))
    a = np.arctan(yw / xw)
    t1 = a + y
    return t1

#theta two
def joint2(xw,yw,leg1,leg2):
    t2 = (np.pi/2) - np.arccos(((leg1**2)+(leg2**2)-(xw**2)-(yw**2))/(2*leg1*leg2))  # add logic to determine what you divide pi by
    return t2

#theta three
def joint3(xw,yw,leg1,leg2,eo):
    eo = np.deg2rad(eo)
    t3 = eo - joint1(xw,yw,leg1,leg2) - joint2(xw,yw,leg1,leg2)  # add logic to add or subtract joint 2 depending on situation
    return t3

def inversek(tx,ty,leg1, leg2, leg3, eo):
    t1 = np.degrees(joint1(wristposx(tx, leg3, eo), wristposy(ty, leg3, eo), leg1, leg2))
    t2 = np.degrees(joint2(wristposx(tx, leg3, eo), wristposy(ty, leg3, eo), leg1, leg2))
    t3 = np.degrees(joint3(wristposx(tx, leg3, eo), wristposy(ty, leg3, eo), leg1, leg2, eo))

    return t1, t2, t3


servos = [2,3,4]

if __name__ == "__main__":
    try:
        working = False
        if (sc.ping(2) == True):  # test the connection
            working = True
            print("working")
        # TODO: Inverse Kinematics
        while working:
            if can_move(servos) == True:
                leg1 = 12.3
                leg2 = 14.8  # lengths of legs in cm
                leg3 = 13.8
                print("Servo2: ", servo2pos(), " Servo3: ", servo3pos(), " Servo4: ", servo4pos())
                print("x: ",(endx(leg1,servo2pos(),leg2,servo3pos(),leg3,servo4pos())))  # print distance from origin
                print("y: ", (endy(leg1, servo2pos(), leg2, servo3pos(), leg3, servo4pos())))  # print h from base
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

                # tx = int(input("Enter Target X: "))
                # ty = int(input("Enter Target Y: "))
                # eo = int(input("Enter End-effector Orientation: "))
                # print(inversek(tx, ty, leg1, leg2, leg3, eo))
            else:
                print("servo moving")
    except:
        print("not working")
        sc.close()
