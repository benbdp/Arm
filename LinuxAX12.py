from pyax12.connection import Connection

sc = Connection(port="/dev/ttyACM0", baudrate=1000000)
# ids = sc.scan()
# for id in ids:
#     print(id)
# sc.close()

id = 1
sc.pretty_print_control_table(id)
sc.close()