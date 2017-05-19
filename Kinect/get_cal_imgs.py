import freenect
import numpy as np
import cv2


def get_ir_video():
    array, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    return array


def get_rgb_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

def get_video():
    array,_ = freenect.sync_get_video(0,freenect.VIDEO_IR_10BIT)
    return array
def pretty_depth(depth):
    np.clip(depth, 0, 2**10-1, depth)
    depth >>=2
    depth=depth.astype(np.uint8)
    return depth


path_ir = "/home/ubuntu/Arm/Kinect/cal_img/ir"
path_rgb = "/home/ubuntu/Arm/Kinect/cal_imgs/rgb"
num = 0
while num < 30:
    #
    # rgb = get_rgb_video()
    # cv2.imwrite(path_rgb + "rgb" + str(num) + ".jpg", rgb)
    # cv2.imshow("rgb", rgb)
    #
    # ir = get_ir_video()
    # cv2.imwrite(path_ir + "ir" + str(num) + ".jpg", rgb)
    # cv2.imshow("ir", ir)
    # get a frame from RGB camera
    frame = get_video()
    # display IR image
    frame = pretty_depth(frame)
    cv2.imshow('IR image', frame)

    num += 1
    k = cv2.waitKey(200) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


#
# def pretty_depth(depth):
#     np.clip(depth, 0, 2**10-1, depth)
#     depth >>=2
#     depth=depth.astype(np.uint8)
#     return depth
# if __name__ == "__main__":
#     while 1:
#         #get a frame from RGB camera
#         frame = get_video()
#         #display IR image
#         frame = pretty_depth(frame)
#         cv2.imshow('IR image',frame)
#
#         # quit program when 'esc' key is pressed
#         k = cv2.waitKey(5) & 0xFF
#         if k == 27:
#             break
#     cv2.destroyAllWindows()