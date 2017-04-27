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

def get_image():
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    return image

num = 100

for i in num:
    cv2.imwrite("/home/pi/apples/"+str(i)+".jpg",get_image())
    time.sleep(0.1)