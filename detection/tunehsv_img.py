import numpy as np
import cv2

img = cv2.imread('/Users/Benjamin/PycharmProjects/Arm/detection/test_images/090822-01-1227c-lg.jpg')


Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow("res",res2)

hsv = cv2.cvtColor(res2,cv2.COLOR_BGR2HSV)

cv2.imshow("hsv",hsv)



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

    result = cv2.bitwise_and(res2,res2,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print(lower)
        break