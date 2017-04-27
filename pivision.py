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

cv2.imwrite("/home/pi/apple.jpg",image)
blurred = cv2.GaussianBlur(image, (5, 5), 2)
# lower = np.array([0, 0, 28])
# upper = np.array([0, 0, 40])

lower = np.array([25, 0, 115])
upper = np.array([35, 5, 125])
mask = cv2.inRange(blurred, lower, upper)
dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=8)
erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=4)
cv2.imshow("mask",mask)

cv2.imshow("erode",erode)
cv2.imshow("dilation",dilation)
cv2.waitKey(0)

im2, contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

len = len(contours)

print("len: ",len)
if len >0:

    center,radius = cv2.minEnclosingCircle(contours[0])

    # x, y, w, h = cv2.boundingRect(contours[0])
    # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


    #
    # print("center: ",center,"radius: ",radius)
    #
    # area = 3.14 * (radius ** 2)
    # print("area: ", area)
    #
    centerx = center[0]

    centerx = int(centerx)

    centery = center[1]

    centery = int(centery)

    radius = int(radius)
    cv2.circle(image,(centerx,centery),radius,(0, 255, 0), 3)


    objectrealmm = 70
    focallen = 3.04
    sensorh = 2.760
    h, w = image.shape[:2]
    #distance_mm = objectrealmm * focallen / objsize

    distance = (focallen*objectrealmm*h)/((radius*2)*sensorh)

    print("distance in mm: ",distance)

#
# circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1.2, 100)
# if circles is not None:
#     # convert the (x, y) coordinates and radius of the circles to integers
#     circles = np.round(circles[0, :]).astype("int")
#
#     # loop over the (x, y) coordinates and radius of the circles
#     for (x, y, r) in circles:
#         # draw the circle in the output image, then draw a rectangle
#         # corresponding to the center of the circle
#         cv2.circle(image, (x, y), r, (0, 255, 0), 4)
#         cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
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
# #
# objectrealmm = 70
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
#cv2.imshow("thresh",thresh)
# cv2.imwrite("/home/pi/hsv.png",hsv)
cv2.imshow("Image", image)
cv2.waitKey(0)