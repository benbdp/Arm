import cv2
import numpy as np
import freenect

""""http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html"""

def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

while True:
    frame = get_video()


    # output = frame.copy()
    frame = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow("edges",edges)
    #
    # # detect circles in the image
    # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    #
    # # ensure at least some circles were found
    # if circles is not None:
    #     # convert the (x, y) coordinates and radius of the circles to integers
    #     circles = np.round(circles[0, :]).astype("int")
    #
    #     # loop over the (x, y) coordinates and radius of the circles
    #     for (x, y, r) in circles:
    #         # draw the circle in the output image, then draw a rectangle
    #         # corresponding to the center of the circle
    #         cv2.circle(output, (x, y), r, (0, 255, 0), 4)
    #         cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    # cv2.imshow("output", output)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()