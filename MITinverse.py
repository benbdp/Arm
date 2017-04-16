import numpy as np

# inputs

l1 = 30

l2 = 20

l3 = 10

eo = 0 # enter degrees

tx = 25.737

ty = 42.221

# convert degrees to rad

eo = np.deg2rad(eo)

print(eo)

# find wrist positions
def wristposx(tx,l3,eo):
    if eo < (np.pi/2):
        xw = tx-l3*(np.cos(eo))
        return xw
    else:
        xw = tx + l3 * (np.cos(eo))
        return xw

print("xw: ",wristposx(tx,l3,eo))

def wristposy(ty,l3,eo):
    yw = ty-l3*(np.sin(eo))
    return yw



print("yw: ",wristposy(ty,l3,eo))

# calculate angle a




#a = np.degrees(a)

#print(a)


# theta one
def joint1(xw,yw,l1,l2):
    y = np.arccos(((xw**2) + (yw**2) + (l1**2) - (l2**2)) / (2 * l1 * np.sqrt((xw**2) + (yw**2))))
    a = np.arctan(yw / xw)
    t1 = a + y
    return t1

#theta two
def joint2(xw,yw,l1,l2):
    t2 = (np.pi/2) -  np.arccos(((l1**2)+(l2**2)-(xw**2)-(yw**2))/(2*l1*l2))  # add logic to determine what you divide pi by
    return t2

#theta three
def joint3(xw,yw,l1,l2,eo):
    t3 = eo -  joint1(xw,yw,l1,l2) - joint2(xw,yw,l1,l2)  # and logic to add or subtract joint 2 depending on situation
    return t3

# convert to degrees and print
t1 = np.degrees(joint1(wristposx(tx,l3,eo),wristposy(ty,l3,eo),l1,l2))
t2 = np.degrees(joint2(wristposx(tx,l3,eo),wristposy(ty,l3,eo),l1,l2))
t3 = np.degrees(joint3(wristposx(tx,l3,eo),wristposy(ty,l3,eo),l1,l2,eo))

print("t1: ",t1)
print("t2: ",t2)
print("t3: ",t3)