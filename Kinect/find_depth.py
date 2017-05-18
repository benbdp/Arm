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


def find_apple(rgb,depth,lower):
    try:
        hsv = cv2.cvtColor(rgb,cv2.COLOR_BGR2HSV)
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

        cv2.circle(rgb,(cx,cy),10,(0,0,255),3)
        cv2.circle(depth,(cx,cy),10,(0,0,255),3)
    except:
        pass

#
# def real_depth:
#     depth, timestamp = freenect.sync_get_depth(0,DEPTH_MM)



if __name__ == "__main__":
    while True:
        # get a frame from RGB camera
        frame = get_video()



        # get a frame from depth sensor
        depth = get_depth()


        #find and draw apple
        find_apple(frame,depth, stored_lower)


        # display RGB image
        cv2.imshow('RGB image', frame)
        # display depth image
        cv2.imshow('Depth image', depth)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()