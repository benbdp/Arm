# import the necessary packages
import cv2
import numpy as np
import freenect


def nothing(x):
    pass


def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)

while True:
    frame = get_video()

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')

    # Normal masking algorithm
    lower = np.array([h,s,v])
    upper = np.array([180,255,255])


    # fooling with mask
    mask = cv2.inRange(hsv,lower, upper)
    # cv2.imshow("msk",mask)
    h, w = mask.shape[:2]

    crop_img = mask[200:h, 0:w]
    dilation = cv2.dilate(crop_img, np.ones((5, 5), np.uint8), iterations=2)
    erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=1)
    cv2.imshow("erode", erode)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        np.save("/home/ubuntu/Arm/Kinect/stored_lower.npy",lower)
        break

cv2.destroyAllWindows()