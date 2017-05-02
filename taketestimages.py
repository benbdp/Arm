# # import the necessary packages
# from picamera.array import PiRGBArray
# from picamera import PiCamera
# import time
# import cv2
# import numpy as np
#
#
# # initialize the camera and grab a reference to the raw camera capture
# camera = PiCamera()
# rawCapture = PiRGBArray(camera)
#
# camera.rotation = 180
#
# # allow the camera to warmup
# time.sleep(0.1)
#
# # grab an image from the camera
#
# def get_image():
#     camera.capture(rawCapture, format="bgr")
#     image = rawCapture.array
#     return image
#
# def video():
#     camera.capture_continuous(rawCapture,format="rgb")
#     frame = rawCapture.array
#     return frame
#
#
# while True:
#     cv2.imshow("img",video())
#     cv2.waitKey(5)
#
#
# # cv2.imshow("img",get_image())
# # cv2.waitKey(5)
# !/usr/bin/env python
import time
import RPi.GPIO as GPIO

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO for camera LED
# Use 5 for Model A/B and 32 for Model B+
CAMLED = 5

# Set GPIO to output
GPIO.setup(CAMLED, GPIO.OUT, initial=False)

# Five iterations with half a second
# between on and off
for i in range(5):
    GPIO.output(CAMLED, True)  # On
    time.sleep(0.5)
    GPIO.output(CAMLED, False)  # Off
    time.sleep(0.5)