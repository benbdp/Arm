import cv2
import numpy as np
import os, sys
import argparse
import glob
"""http://stackoverflow.com/questions/7427101/dead-simple-argparse-example-wanted-1-argument-3-results"""

parser = argparse.ArgumentParser(description="An argparse example")
parser.add_argument('type', help='enter rgb or ir', nargs='?', default="check_string_for_empty")
args = parser.parse_args()

if args.type == 'check_string_for_empty':
    print ('You need to enter rgb or ir')

elif args.type == "rgb":
    print("You asked for rgb calibration")

    path = "/home/ubuntu/Arm/Kinect/cal_imgs/rgb/"
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6 * 9, 3), np.float32)
    objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.
    images = glob.glob(os.path.join(path, '*.jpg'))
    num = 1
    for fname in images:
        print (num)

        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape[:2]
        print("h: ",h)
        print("w: ",w)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
        print(ret)
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (9, 6), corners2, ret)
            # cv2.imshow('img',img)
            # cv2.waitKey(100)
            num = num + 1
    height = input("enter what was printed for h")
    width = input("enter what was printed for w")

    retval, camera_matrix, dist_coefs, rotationvector, translationvector = cv2.calibrateCamera(objpoints, imgpoints, (width, height), None,None)


    print('matrix', camera_matrix)
    print('dist', dist_coefs)

    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rotationvector[i], translationvector[i], camera_matrix,
                                          dist_coefs)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
        mean_error += error

    print ("mean error: ", mean_error / len(objpoints))

    for fname in images:
        img = cv2.imread(fname)

        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

        dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

        cv2.imshow('undistort',dst)
        cv2.waitKey()


elif args.type == "ir":
    print("You asked for ir calibration")
    path = "/home/ubuntu/Arm/Kinect/cal_imgs/ir/"
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6 * 9, 3), np.float32)
    objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.
    images = glob.glob(os.path.join(path, '*.jpg'))
    num = 1
    for fname in images:
        print(num)

        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape[:2]
        print("h: ", h)
        print("w: ", w)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
        print(ret)
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (9, 6), corners2, ret)
            # cv2.imshow('img',img)
            # cv2.waitKey(100)
            num = num + 1
    height = input("enter what was printed for h")
    width = input("enter what was printed for w")

    retval, camera_matrix, dist_coefs, rotationvector, translationvector = cv2.calibrateCamera(objpoints, imgpoints,
                                                                                               (width, height), None,
                                                                                               None)

    print('matrix', camera_matrix)
    print('dist', dist_coefs)

    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rotationvector[i], translationvector[i], camera_matrix,
                                          dist_coefs)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
        mean_error += error

    print("mean error: ", mean_error / len(objpoints))

    for fname in images:
        img = cv2.imread(fname)

        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

        dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

        cv2.imshow('undistort', dst)
        cv2.waitKey()

else:
    print("You made invalid entry")