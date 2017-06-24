import numpy as np
import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('/Users/Benjamin/PycharmProjects/Arm/stereo/opencv-feature-matching-template.jpg',0)
img2 = cv2.imread('/Users/Benjamin/PycharmProjects/Arm/stereo/opencv-feature-matching-image.jpg',0)

IN_MATCH_COUNT = 10

# Initiate SIFT detector
sift = cv2.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

#
# φ0 = 61.37 # calculated based on this link: http://vrguy.blogspot.com/2013/04/converting-diagonal-field-of-view-and.html
# b = 10 # distance between cameras in mm
# x0 = 1280 # number of horizontal pixels
# n = 0
# k = 0
# m = 0
#
# diff = (n/2)+k-1-(m/2)
#
# d = (b * x0)/(2*np.tan(φ0/2)*diff)




