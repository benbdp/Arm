import cv2
import numpy as np
import sys



def hsv(img):
   return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



try:
    vidStream = cv2.VideoCapture(0)  # index of your camera
except:
    print("problem opening input stream")
    sys.exit(1)


while True:
    ret, frame = vidStream.read()
    blur = cv2.GaussianBlur(frame, (5, 5), 5)
    HSV = hsv(blur)
    cv2.imshow("frame",frame)
    cv2.imshow("hsv",HSV)

    lower_range = np.array([150, 200, 150])  # define range of color in HSV
    upper_range = np.array([190, 250, 190])
    mask = cv2.inRange(HSV, lower_range, upper_range)

    cv2.imshow("mask",mask)

    cv2.waitKey(5)

    break
