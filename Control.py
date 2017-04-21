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

try:
    working = False
    if (sc.ping(2) == True):
        working = True
        print("working")

    while working:
        servonum = input("Enter servo num")
        servonum = int(servonum)
        angle = input("Enter angle")
        angle = int(angle)

        if servonum == 2:
            servo2(angle)

        elif servonum == 3:
            servo3(angle)

        elif servonum == 4:
            servo4(angle)

        time.sleep(1)

except:
    print("not working")
    sc.close()
