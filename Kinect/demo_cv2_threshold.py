#!/usr/bin/env python

"""https://github.com/OpenKinect/libfreenect/blob/master/wrappers/python/demo_cv2_threshold.py"""

import freenect
import cv2
import frame_convert2
import numpy as np


threshold = 100
current_depth = 500
#
#
# def change_threshold(value):
#     global threshold
#     threshold = value
#
#
# def change_depth(value):
#     global current_depth
#     current_depth = value


def show_depth():
    # global threshold
    # global current_depth

    depth, timestamp = freenect.sync_get_depth()
    depth = 255 * np.logical_and(depth >= current_depth - threshold,
                                 depth <= current_depth + threshold)
    depth = depth.astype(np.uint8)
    cv2.imshow('Depth', depth)


def show_video():
    cv2.imshow('Video', frame_convert2.video_cv(freenect.sync_get_video()[0]))


# cv2.namedWindow('Depth')
# cv2.namedWindow('Video')
# cv2.createTrackbar('threshold', 'Depth', threshold,     500,  change_threshold)
# cv2.createTrackbar('depth',     'Depth', current_depth, 2048, change_depth)

print('Press ESC in window to stop')


while 1:
    show_depth()
    show_video()
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()