import freenect
import numpy as np
import cv2
import argparse

"""http://stackoverflow.com/questions/7427101/dead-simple-argparse-example-wanted-1-argument-3-results"""
parser = argparse.ArgumentParser(description="Program to take calibration images for Kinect")
parser.add_argument('camera', help='Enter rgb or ir', nargs='?', default="check_string_for_empty")
args = parser.parse_args()


def get_ir_video():
    array, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    return array


def get_rgb_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


def pretty_depth(depth):
    np.clip(depth, 0, 2**10-1, depth)
    depth >>=2
    depth=depth.astype(np.uint8)
    return depth

if args.camera == 'check_string_for_empty':
    print ('Enter rgb or ir at the end')

elif args.camera == "rgb":
    print("Taking rgb images")
    path_rgb = "/home/ubuntu/Arm/Kinect/cal_imgs/rgb/"
    num = 0
    while True:
        rgb = get_rgb_video()
        cv2.imwrite(path_rgb + "rgb" + str(num) + ".jpg", rgb)
        cv2.imshow("rgb", rgb)
        num += 1
        k = cv2.waitKey(2000) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

elif args.camera == "ir":
    print("Taking ir images")
    path_ir = "/home/ubuntu/Arm/Kinect/cal_imgs/ir/"
    num = 0
    while True:
        ir = get_ir_video()
        ir = pretty_depth(ir)
        ir = cv2.GaussianBlur(ir, (5, 5), 5)
        cv2.imwrite(path_ir + "ir" + str(num) + ".jpg", ir)
        cv2.imshow("ir", ir)
        num += 1
        k = cv2.waitKey(2000) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

else:
    print("You made invalid entry")



