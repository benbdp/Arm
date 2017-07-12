import cv2
import numpy as np
import time

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_EXPOSURE,0.5)
print(camera.get(cv2.CAP_PROP_EXPOSURE))


while True:
    _, frame = camera.read()
    start = time.time().now()
    print(start)
    cv2.imshow("frame",frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break