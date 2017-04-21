from pyax12.connection import Connection

sc = Connection(port="/dev/ttyACM0", baudrate=1000000)
ids = sc.scan()
for id in ids:
    print(id)
sc.close()