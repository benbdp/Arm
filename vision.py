import cv2
import numpy as np
import sys



def hsv(img):
   return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



try:
    vidStream = cv2.VideoCapture(0)  # index of your camera
except:
    print("problem opening input stream")
    sys.exit(1)





if __name__ == "__main__":
    run = True
    focal_length = 1032.78
    while run:
        ret, frame = vidStream.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv",hsv)
        edges = cv2.Canny(hsv, 100, 200)
        cv2.imshow("edges",edges)


        # huesatval = hsv(frame)
        # lower = np.array([110, 50, 50])
        # upper = np.array([130, 255, 255])
        # mask = cv2.inRange(huesatval, lower, upper)
        # cv2.imshow("mask",mask)
        # dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=6)
        # erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=6)
        # im2, contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # newcontours = []
        # for cnt in contours:
        #     area = cv2.contourArea(cnt)
        #     print(area)
        #     if area > 2:
        #         newcontours.append(cnt)
        # num_contours = len(newcontours)
        # print("num contours: ",num_contours)

        #center,radius = cv2.minEnclosingCircle(newcontours[0])

        # area = 3.14 *radius**2
        # print(area)



        #cv2.circle(frame,int(center),int(radius),(0, 255, 0), 3)


       # distance_mm = objectrealmm * focallen / objsize

        #
        # cv2.imshow("edited",erode)
        # #cv2.putText(frame,str(center),(frame.shape[1] - 800, frame.shape[0] - 100), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
        # cv2.imshow("frame",frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break