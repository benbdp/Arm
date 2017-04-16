import numpy as np

AB = 30
BC = 20
CT = 10
angle = 27.2
rangle = np.deg2rad(angle)

print("rangle",rangle)

Tx,Ty = 10,10

Cx = Tx+CT*np.cos(rangle)
Cy = Ty+CT*np.sin(rangle)


print(Cx,Cy)

AC = np.sqrt((Cx**2)+(Cy**2))

print(AC)

AC_angle = np.arctan((Cy)/(Cx))
print(AC_angle)

AC_angle = np.degrees(AC_angle)

print(AC_angle)

s = (AB+BC+AC)/2
print("s",s)

SA = np.sqrt(s*((s-AB)*(s-BC)*(s-AC)))
print("SA",SA)


A=np.arcsin(2*SA/(AB*AC))

B=np.arcsin(2*SA/(AB*BC))

#C=np.arcsin((2*SA)/(AC/BC))

servo_A = AC_angle + A
print(servo_A)
servo_B = B
print(servo_B)
servo_C = angle - servo_B - servo_A
print(servo_C)

