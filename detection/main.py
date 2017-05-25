import cv2
import numpy as np


img = cv2.imread("/Users/Benjamin/PycharmProjects/Arm/detection/test_images/tomato-plant-supports_full_width.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
cv2.imshow('hsv',hsv)
cv2.imshow('img',img)




def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)

while True:
    frame = hsv
    frame = cv2.GaussianBlur(frame, (5, 5), 5)

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

    dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=2)
    erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=1)
    cv2.imshow("erode", erode)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        np.save("/home/ubuntu/Arm/Kinect/stored_lower.npy",lower)
        break







#
# def nothing(x):
#     pass
#
#
# # Creating a window for later use
# cv2.namedWindow('result')
#
# # Starting with 100's to prevent error while masking
# h,s,v = 100,100,100
#
# # Creating track bar
# cv2.createTrackbar('h', 'result',0,179,nothing)
# cv2.createTrackbar('s', 'result',0,255,nothing)
# cv2.createTrackbar('v', 'result',0,255,nothing)
#
# while True:
#
#     #converting to HSV
#     hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
#     # get info from track bar and appy to result
#     h = cv2.getTrackbarPos('h','result')
#     s = cv2.getTrackbarPos('s','result')
#     v = cv2.getTrackbarPos('v','result')
#
#     # Normal masking algorithm
#     lower = np.array([h,s,v])
#     upper = np.array([180,255,255])
#
#
#     # fooling with mask
#     mask = cv2.inRange(hsv,lower, upper)
#
#     dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=2)
#     erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=1)
#     cv2.imshow("erode", erode)
#
#     result = cv2.bitwise_and(img,img,mask = mask)
#
#     cv2.imshow('result',result)
#
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break

cv2.destroyAllWindows()