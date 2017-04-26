import numpy as np
import cv2
apple_cascade = cv2.CascadeClassifier('/Users/Benjamin/PycharmProjects/Arm/applecascade.xml')
img = cv2.imread('/Users/Benjamin/PycharmProjects/Arm/apples/apple1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
apples = apple_cascade.detectMultiScale(gray, 1.3, 3)
for (x,y,w,h) in apples:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()