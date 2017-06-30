import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)

def home_a():
    ser.write(bytes(str(9999)+"a,", encoding="ascii"))
    while ser.readline().decode('ascii').rstrip() != "Reached A":
        pass
    print("At A Home")

def home_b():
    ser.write(bytes(str(9999) + "d,", encoding="ascii"))
    while ser.readline().decode('ascii').rstrip() != "Reached B":
        pass
    print("At B Home")

def setup():
    while len(ser.readline().decode('ascii').rstrip()) == 0:
        pass
    print("Connected!")

def move(num):
    ser.write(bytes(str(num) + "d,", encoding="ascii"))



if __name__ == "__main__":
    try:
        setup()
        stat = True
        while stat:
            entry = input("Entry: ")
            if entry == "a":
                home_a()
            if entry == "b":
                home_b()
            else:
                stat = False
    except:
        ser.close()
        print("Unexpected error:", sys.exc_info()[0])
        raise
