from pyax12.connection import Connection
import time

sc = Connection(port='/dev/ttyACM0', baudrate=1000000)


def servo2(pos):
    if angle < 0:
        print("illegal pos")
    elif pos > 0:
        pos = -pos
        sc.goto(2, pos, 100, True)

    elif pos == 0:
        print("is zero")
        sc.goto(2, pos, 100, True)


def servo3(pos):
    sc.goto(3, pos, 100, True)

def servo4(pos):
    if pos < 0:
        pos = abs(pos)
        print("should move below")
    elif pos > 0:
        pos = -pos
        print("should move above")

    elif pos == 0:
        print("is zero")
    else:
       print("invalid entry")
    sc.goto(4, pos, 100, True)


try:
    working = False
    if (sc.ping(2) == True):
        working = True
        print("working")

    while working:
        # servonum = input("Enter servo num")
        # servonum = int(servonum)
        angle = input("Enter angle")
        angle = int(angle)

        servo2(angle)

        #
        # if servonum == 2:
        #     servo2(angle)
        #
        # if servonum == 3:
        #     servo3(angle)
        #
        # if servonum == 4:
        #     servo4(angle)

        time.sleep(1)

except:
    print("not working")
    sc.close()
