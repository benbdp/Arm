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

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



edges = cv2.Canny(gray,100,200)

circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1.2, 200)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',image)
#
# lower = np.array([105, 145, 130])
# upper = np.array([115, 165, 145])
# mask = cv2.inRange(hsv, lower, upper)
# dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=1)
# erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=1)

#
# im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# newcontours = []
# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     if area > 200:
#         newcontours.append(cnt)
#         area = cv2.contourArea(cnt)
#         print(area)

# center,radius = cv2.minEnclosingCircle(newcontours[0])
# #
# # print("center: ",center,"radius: ",radius)
# #
# # area = 3.14 * (radius ** 2)
# # print("area: ", area)
# #
# centerx = center[0]
#
# centerx = int(centerx)
#
# centery = center[1]
#
# centery = int(centery)
#
# radius = int(radius)
# cv2.circle(image,(centerx,centery),radius,(0, 255, 0), 3)
#
# objectrealmm = 50.8
# focallen = 3.04
# sensorh = 2.760
# h, w = image.shape[:2]
# #distance_mm = objectrealmm * focallen / objsize
#
# distance = (focallen*objectrealmm*h)/((radius*2)*sensorh)
#
# print("distance in mm: ",distance)

# cv2.imshow("erode",erode)
# cv2.imshow("mask",mask)
cv2.imshow("gray",gray)
cv2.imshow("edge",edges)
# cv2.imwrite("/home/pi/hsv.png",hsv)
# cv2.imshow("Image", image)
cv2.waitKey(0)