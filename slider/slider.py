import serial

ser = serial.Serial('COM6',baudrate=9600,timeout=1)


def forward():
    ser.write(b'f')

def backward():
    ser.write(b'b')

def get_return():
    ret = ser.readline().decode('ascii')
    ret = ret.rstrip()
    return ret

def get_real_return():
    while len(get_return()) ==0:
        get_return()
    return get_return()


if __name__ == "__main__":
    try:
        while True:
            forward()
            print(get_return())
            # entry = input("Enter f or b: ")
            # if entry == 'f':
            #     status = True
            #     while status:
            #         forward()
            #         if get_real_return() == 'g':
            #             status = True
            #         elif get_real_return() == 'b':
            #             status = False
            #     print("error")



    except:
        ser.close()