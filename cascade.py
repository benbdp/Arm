import numpy as np
import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# this is the cascade we just made. Call what you want
# watch_cascade = cv2.CascadeClassifier('watchcascade10stage.xml')

apple_cascade = cv2.CascadeClassifier("/Users/Benjamin/PycharmProjects/Arm/bananacascade.xml")

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    apples = apple_cascade.detectMultiScale(gray, 2, 5)

    # add this
    # image, reject levels level weights.
    # watches = watch_cascade.detectMultiScale(gray, 50, 50)

    # add this
    for (x, y, w, h) in apples:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Banana', (x , y), font, 0.5, (11, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()