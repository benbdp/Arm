import freenect
import time
import random
import signal

led = random.randint(0, 6)
tilt = random.randint(0, 30)
freenect.set_led(freenect.DevPtr,led)
freenect.set_tilt_degs(freenect.DevPtr, tilt)
print('led[%d] tilt[%d] accel[%s]' % (led, tilt, freenect.get_accel(freenect.DevPtr)))