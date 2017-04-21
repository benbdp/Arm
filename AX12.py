import Pynamixel


hardware = Pynamixel.hardwares.USB2AX("/dev/ttyACM0", 1000000)
system = Pynamixel.System(Pynamixel.Bus(hardware))
servo0 = system.add_device(Pynamixel.devices.AX12, 0)
servo1 = system.add_device(Pynamixel.devices.AX12, 1)
servo2 = system.add_device(Pynamixel.devices.AX12, 2)
servo3 = system.add_device(Pynamixel.devices.AX12, 3)


def deg2hex(degree):
    max_lim = 1023
    min_lim = 0
    decimal = int((256 * degree) / 75)
    if decimal > max_lim:
        pass
    elif decimal < min_lim:
        pass
    else:
        pos = hex(decimal)
        return pos


def set_servo0(degree):
    hex_val = deg2hex(degree)
    servo0.goal_position.write(hex_val)


def set_servo1(degree):
    hex_val = deg2hex(degree)
    servo1.goal_position.write(hex_val)


def set_servo2(degree):
    hex_val = deg2hex(degree)
    servo2.goal_position.write(hex_val)


def set_servo3(degree):
    hex_val = deg2hex(degree)
    servo3.goal_position.write(hex_val)