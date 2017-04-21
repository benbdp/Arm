from pyax12.connection import Connection
import time
sc = Connection(port="/dev/ttyACM0", baudrate=1000000)
id = 1
sc.goto(id, 0, speed=512, degrees=True)
time.sleep(1)
sc.goto(id, -45, speed=512, degrees=True)
sc.close()