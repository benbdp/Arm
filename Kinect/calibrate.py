import cv2
import numpy as np
import os, sys
import argparse
"""http://stackoverflow.com/questions/7427101/dead-simple-argparse-example-wanted-1-argument-3-results"""

parser = argparse.ArgumentParser(description="An argparse example")

parser.add_argument('type', help='enter rgb or ir', nargs='?', default="check_string_for_empty")

args = parser.parse_args()

if args.type == 'check_string_for_empty':
    print ('I can tell that no argument was given and I can deal with that here.')
elif args.type == "rgb":
    print("You asked for rgb calibration")
elif args.type == "ir":
    print("You asked for ir calibration")
else:
    print("You made invalid entry")


#
# if args['type'] == "rgb":
#     print("rgb cal")
#
# elif args['type'] == "ir":
#     print("ir cal")
#
# elif args
#
# else:
#     print("invalid entry")
#




# if args.ir:
#     print ("ir calibration")
#
# elif args.rgb:
#     print("rgb calibration")