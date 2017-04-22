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
cv2.imshow("mask",mask)
#cv2.imwrite("/home/pi/hsv.png",hsv)

# display the image on screen and wait for a keypress
cv2.imshow("hsv",hsv)
cv2.imshow("Image", image)
cv2.waitKey(0)