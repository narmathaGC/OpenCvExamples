### run code by using command "python readImageandWrite.py -p input.jpg"

import cv2
import argparse

# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-p','--imagePath', help='mention image absolute path')
args = parser.parse_args()


image = cv2.imread(args.imagePath)
# show in output window
cv2.imshow("input-image",image);cv2.waitKey(0)
# write image
cv2.imwrite("out.jpg",image)


