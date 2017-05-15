"""From: https://naman5.wordpress.com/2014/06/24/experimenting-with-kinect-using-opencv-python-and-open-kinect-libfreenect/"""

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


# function to get depth image from kinect
def get_depth():
    array, _ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array


def find_apple(img,lower):
    try:
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
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

        M = cv2.moments(newcontours[0])
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        cv2.circle(img,(cx,cy),10,(0,0,255),3)
        return cx,cy
    except:
        pass


def draw_on_depth(x,y,img):
    try:
        cv2.circle(img, (x, y), 10, (0, 0, 255), 3)
    except:
        pass



if __name__ == "__main__":
    while True:
        # get a frame from RGB camera
        frame = get_video()

        cx,cy = find_apple(frame,stored_lower)

        # get a frame from depth sensor
        depth = get_depth()

        draw_on_depth(cx,cy,depth)

        # display RGB image
        cv2.imshow('RGB image', frame)
        # display depth image
        cv2.imshow('Depth image', depth)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()