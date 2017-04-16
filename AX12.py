import numpy
import Pynamixel


hardware = Pynamixel.hardwares.USB2AX("/dev/ttyACM0", 1000000)
system = Pynamixel.System(Pynamixel.Bus(hardware))
servo = system.add_device(Pynamixel.devices.AX12, 2)
print(servo.present_position.read())



# degree = 150
#
#
# def deg2hex(degree):
#     max_lim = 1023
#     min_lim = 0
#     decimal = int((256 * degree) / 75)
#     print(decimal)
#     if decimal > max_lim:
#         pass
#     elif decimal < min_lim:
#         pass
#     else:
#         pos = hex(decimal)
#         print(pos)
#
#
# deg2hex(degree)



# 0 = 0x000
# 150 = 0x200
# 300 = 0x3ff