import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM1',baudrate=9600,timeout=1)

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


if __name__ == "__main__":
    try:
        while len(ser.readline().decode('ascii').rstrip()) == 0:
            pass
        print("Connected!")
        home_b()
    except:
        ser.close()
        print("Unexpected error:", sys.exc_info()[0])
        raise
