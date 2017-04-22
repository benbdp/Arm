# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

camera.rotation = 180

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower = np.array([90, 155, 75])
upper = np.array([105, 165, 85])
mask = cv2.inRange(hsv, lower, upper)
dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=6)
erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=6)


im2, contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
newcontours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1300:
        newcontours.append(cnt)
        area = cv2.contourArea(cnt)
        print(area)

center,radius = cv2.minEnclosingCircle(newcontours[0])

print("center: ",center,"radius: ",radius)

area = 3.14 * (radius ** 2)
print("area: ", area)

cv2.imshow("erode",erode)
# cv2.imshow("mask",mask)
# cv2.imshow("hsv",hsv)
# cv2.imshow("Image", image)
cv2.waitKey(0)