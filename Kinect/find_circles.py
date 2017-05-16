import cv2
import numpy as np
import freenect

""""http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html"""

def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

while True:
    frame = get_video()
    frame = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()