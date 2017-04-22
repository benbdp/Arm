import numpy as np

# inputs

leg1 = 30

leg2 = 20

leg3 = 10

eo = 0 # enter degrees

tx = 25.737

ty = 42.221

# find wrist positions
def wristposx(tx,leg3,eo):
    eo = np.deg2rad(eo)
    if eo < (np.pi/2):
        xw = tx-leg3*(np.cos(eo))
        return xw
    else:
        xw = tx + leg3 * (np.cos(eo))
        return xw

print("xw: ",wristposx(tx,leg3,eo))

def wristposy(ty,leg3,eo):
    eo = np.deg2rad(eo)
    yw = ty-leg3*(np.sin(eo))
    return yw



print("yw: ",wristposy(ty,leg3,eo))

# calculate angle a




#a = np.degrees(a)

#print(a)


# theta one
def joint1(xw,yw,leg1,leg2):
    y = np.arccos(((xw**2) + (yw**2) + (leg1**2) - (leg2**2)) / (2 * leg1 * np.sqrt((xw**2) + (yw**2))))
    a = np.arctan(yw / xw)
    t1 = a + y
    return t1

#theta two
def joint2(xw,yw,leg1,leg2):
    t2 = (np.pi/2) - np.arccos(((leg1**2)+(leg2**2)-(xw**2)-(yw**2))/(2*leg1*leg2))  # add logic to determine what you divide pi by
    return t2

#theta three
def joint3(xw,yw,leg1,leg2,eo):
    eo = np.deg2rad(eo)
    t3 = eo - joint1(xw,yw,leg1,leg2) - joint2(xw,yw,leg1,leg2)  # add logic to add or subtract joint 2 depending on situation
    return t3

# # convert to degrees and print
# t1 = np.degrees(joint1(wristposx(tx,leg3,eo),wristposy(ty,leg3,eo),leg1,leg2))
# t2 = np.degrees(joint2(wristposx(tx,leg3,eo),wristposy(ty,leg3,eo),leg1,leg2))
# t3 = np.degrees(joint3(wristposx(tx,leg3,eo),wristposy(ty,leg3,eo),leg1,leg2,eo))



def inversek(tx,ty,leg1, leg2, leg3, eo):
    t1 = np.degrees(joint1(wristposx(tx, leg3, eo), wristposy(ty, leg3, eo), leg1, leg2))
    t2 = np.degrees(joint2(wristposx(tx, leg3, eo), wristposy(ty, leg3, eo), leg1, leg2))
    t3 = np.degrees(joint3(wristposx(tx, leg3, eo), wristposy(ty, leg3, eo), leg1, leg2, eo))

    return t1, t2, t3