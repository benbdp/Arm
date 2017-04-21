from pyax12.connection import Connection
import time

sc = Connection(port='/dev/ttyACM0', baudrate=1000000)

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

        if servonum == 2 and angle > 0:
            sc.goto(2, -angle, 100, True)
        elif servonum == 2 and angle < 0:
            pass
            print("illegal pos")

        if servonum == 4 and angle > 0:
            sc.goto(4, -angle, 100, True)

        elif servonum == 4 and angle < 0:
            sc.goto(4, abs(angle), 100, True)

        else:
            sc.goto(servonum, angle, 100, True)

        time.sleep(1)

except:
    print("not working")
    sc.close()
