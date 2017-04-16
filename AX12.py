import numpy
import Pynamixel


# hardware = Pynamixel.hardwares.USB2AX("/dev/ttyACM0", 1000000)
# system = Pynamixel.System(Pynamixel.Bus(hardware))
# servo = system.add_device(Pynamixel.devices.AX12, 1)
# servo.goal_position.write(0x200)
# servo.moving.read()
max_lim = 1023
min_lim = 0

degree = 280

decimal = int((256 * degree) / 75)
print(decimal)

if decimal > max_lim:
    pass
elif decimal < min_lim:
    pass
else:
    pos = hex(decimal)
    print(pos)




# 0 = 0x000
# 150 = 0x200
# 300 = 0x3ff