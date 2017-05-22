import numpy as np
import cv2

img = cv2.imread('/Users/Benjamin/PycharmProjects/Arm/detection/test_images/tomato-plant.jpg')
output = img.copy()
img = cv2.GaussianBlur(img, (5, 5), 8)






# img = cv2.GaussianBlur(img, (5, 5), 2)

cv2.imshow("orig",img)




print(img)

row, col, ch = img.shape



for rownum in range(len(img)):
   for colnum in range(len(img[rownum])):
       maximum = img[rownum][colnum].argmax(0)

       if maximum == 0:
           img[rownum][colnum] = [0, 0, 0]

       elif maximum == 1:
           img[rownum][colnum] = [0, 0, 0]

       elif maximum == 2:
           img[rownum][colnum] = [255, 255, 255]

print(img)

img = cv2.dilate(img,(5,5),iterations=4)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 10, 200)

cv2.imshow("edge",edged)

circles = cv2.HoughCircles(edged, cv2.HOUGH_GRADIENT, 1, 60,
                           param1=30, param2=30, minRadius=10, maxRadius=400)
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

cv2.imshow("img",img)
cv2.imshow('output',output)
cv2.waitKey()

#
# ## plan: iterate over image turn pixels that are mostly red -red mostly green -green and mostly blue -blue
