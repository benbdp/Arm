import cv2
import numpy as np

cap = cv2.VideoCapture(0)



while True:
    frame = cap.read()
    cv2.imshow("frame",frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break