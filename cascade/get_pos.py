# import the necessary modules
import freenect
import cv2
import numpy as np


stored_lower = np.load("/home/ubuntu/Arm/Kinect/stored_lower.npy")

# function to get RGB image from kinect
def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


def find_apple(rgb,lower):
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
        crop_img = rgb[y-4: y + h+4, x-4: x + w+4]
        h, w = crop_img.shape[:2]
        print h,w

        return crop_img
        #
        #
        # x, y, w, h = cv2.boundingRect(newcontours[0])
        # cv2.rectangle(rgb, (x-3, y-3), (x + w+3, y + h+3), (0, 255, 0), 2)

    except:
        pass



if __name__ == "__main__":
    while True:
        # get a frame from RGB camera
        frame = get_video()
        cv2.imshow('window', frame)


        #find and draw apple
        apple = find_apple(frame,stored_lower)


        # display RGB image
        cv2.imshow('window with circles', apple)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()