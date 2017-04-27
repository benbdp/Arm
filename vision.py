import time
import cv2
import numpy as np
import sys


camera = cv2.VideoCapture(0)
def get_image():
    retval, img = camera.read()
    return img


img = get_image()
cv2.imshow("img",img)
newimg = cv2.cvtColor()
blurred = cv2.GaussianBlur(img, (5, 5), 2)
# lower = np.array([0, 0, 28])
# upper = np.array([0, 0, 40])              #Worked on the bus
# mask = cv2.inRange(blurred, lower, upper)
image_blur_hsv = cv2.cvtColor(blurred, cv2.COLOR_RGB2HSV)

# Filter by colour
    # 0-10 hue
    # minimum red amount, max red amount
min_red = np.array([0, 100, 80])
max_red = np.array([10, 256, 256])
    # layer
mask1 = cv2.inRange(image_blur_hsv, min_red, max_red)

    # birghtness of a color is hue
    # 170-180 hue
min_red2 = np.array([170, 100, 80])
max_red2 = np.array([180, 256, 256])
mask2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)

    # looking for what is in both ranges
    # Combine masks
mask = mask1 + mask2
dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=5)
erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=3)
cv2.imshow("mask",mask)

cv2.imshow("erode",erode)
cv2.imshow("dilation",dilation)
cv2.waitKey()

im2, contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

newcontours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    print(area)
    if area > 400:
        newcontours.append(cnt)
num_contours = len(newcontours)
print("num contours: ",num_contours)

if num_contours >0:

    center,radius = cv2.minEnclosingCircle(newcontours[0])

    # x, y, w, h = cv2.boundingRect(contours[0])
    # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


    #
    # print("center: ",center,"radius: ",radius)
    #
    # area = 3.14 * (radius ** 2)
    # print("area: ", area)
    #
    centerx = center[0]

    centerx = int(centerx)

    centery = center[1]

    centery = int(centery)

    radius = int(radius)
    cv2.circle(img,(centerx,centery),radius,(0, 255, 0), 3)
    #
    #
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #
    # edges = cv2.Canny(gray,100,200)
    #
    #
    # et, dst = cv2.threshold(gray,60, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("edges",edges)

    # cv2.imshow("gray",gray)
    # cv2.imshow("dst",dst)
    cv2.imshow("img",img)

    cv2.waitKey()
    cv2.destroyAllWindows()







#
#
# def hsv(img):
#    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#
#
# try:
#     vidStream = cv2.VideoCapture(0)  # index of your camera
# except:
#     print("problem opening input stream")
#     sys.exit(1)
#
#
#
#
#
# if __name__ == "__main__":
#     run = True
#     focal_length = 1032.78
#     while run:
#         ret, frame = vidStream.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         cv2.imshow("hsv",hsv)
#         edges = cv2.Canny(hsv, 100, 200)
#         cv2.imshow("edges",edges)
#
#
#         # huesatval = hsv(frame)
#         # lower = np.array([110, 50, 50])
#         # upper = np.array([130, 255, 255])
#         # mask = cv2.inRange(huesatval, lower, upper)
#         # cv2.imshow("mask",mask)
#         # dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=6)
#         # erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=6)
#         # im2, contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         # newcontours = []
#         # for cnt in contours:
#         #     area = cv2.contourArea(cnt)
#         #     print(area)
#         #     if area > 2:
#         #         newcontours.append(cnt)
#         # num_contours = len(newcontours)
#         # print("num contours: ",num_contours)
#
#         #center,radius = cv2.minEnclosingCircle(newcontours[0])
#
#         # area = 3.14 *radius**2
#         # print(area)
#
#
#
#         #cv2.circle(frame,int(center),int(radius),(0, 255, 0), 3)
#
#
#        # distance_mm = objectrealmm * focallen / objsize
#
#         #
#         # cv2.imshow("edited",erode)
#         # #cv2.putText(frame,str(center),(frame.shape[1] - 800, frame.shape[0] - 100), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
#         # cv2.imshow("frame",frame)
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord("q"):
#             break