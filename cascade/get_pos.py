import cv2
import numpy as np
import time
import freenect

def fix_pos(frame,path):
        num = 0
        while True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, dst = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
            dilation = cv2.dilate(dst, np.ones((5, 5), np.uint8), 1)
            im, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            newcontours = []
            for i in contours:
                area = cv2.contourArea(i)
                if area > 100:  # run test to ensure small contours are eliminated
                    newcontours.append(i)
            x, y, w, h = cv2.boundingRect(newcontours[0])
            print(x,y,w,h)
            crop_img = frame[y: y + h, x: x + w]
            h, w = crop_img.shape[:2]
            resized_image = cv2.resize(crop_img, (w, h))
            cv2.imwrite(path + "tom" + str(num) + ".jpg", resized_image)
            num += 1
            time.sleep(1)

def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

path = "/home/ubuntu/Arm/cascade/pics"
# frame = get_video()
# tom_pos(frame,path)
while True:
    frame = get_video()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    dilation = cv2.dilate(dst, np.ones((5, 5), np.uint8), 1)
    cv2.imshow("window",dilation)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()