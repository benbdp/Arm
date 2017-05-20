import cv2
import numpy as np
import time
import glob
import os


stored_lower = np.load("/home/ubuntu/Arm/Kinect/stored_lower.npy")

def find_apple(rgb,lower,file):
    try:
        blur = cv2.blur(rgb, (5, 5))
        hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        upper = np.array([180,255,255])
        mask = cv2.inRange(hsv,lower,upper)
        dilation = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=2)  # dilate pixels to fill in gaps
        erode = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=1)  # cut away border pixels to reduce size
        im2, contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # contour detection
        newcontours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            # print "area", area
            if area > 400:  # run test to ensure small contours are eliminated
                newcontours.append(cnt)
        x, y, w, h = cv2.boundingRect(newcontours[0])
        crop_img = rgb[y-2: y + h+2, x-2: x + w+2]
        # h, w = crop_img.shape[:2]            #w    h
        # resized_image = cv2.resize(crop_img, (48, 50))

        return crop_img,x,y,w,h
    except:
        pass

if __name__ == "__main__":
    path = "/home/ubuntu/Arm/cascade/pos/"
    frames = glob.glob(os.path.join(path, '*.jpg'))
    file = open("/home/ubuntu/Arm/cascade/testfile.txt", "w+")
    try:
        while True:
            for fn in frames:
                print('processing %s... ' % fn)
                img = cv2.imread(fn)
                img = cv2.resize(img, (100, 100))
                cv2.imshow("img",img)


                #find and draw apple
                apple,x,y,w,h = find_apple(img,stored_lower,file)
                file.write('x:'+str(x))
                cv2.imshow('window', apple)
                cv2.waitKey(1000)
    except:
        print "error"
        file.close()