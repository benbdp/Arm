import numpy as np
import cv2
import freenect

# this is the cascade we just made. Call what you want
cascade = cv2.CascadeClassifier('/home/ubuntu/Arm/cascade/data/cascade.xml')

def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

while 1:
    img = get_video()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # add this
    # image, reject levels level weights.
    apple = cascade.detectMultiScale(gray, 20, 2)

    # add this
    for (x, y, w, h) in apple:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
