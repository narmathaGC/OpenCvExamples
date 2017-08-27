### run code by using command "python histogramEqualization.py -p input.jpg"
# Histogram equalization is good when histogram of the image is confined to a particular region. 
# It won't work good in places where there is large intensity variations where histogram covers a large region, ie both bright and dark pixels are present

import cv2
import numpy as np
import argparse

# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-p','--imagePath', help='mention rgb image absolute path')
args = parser.parse_args()


def histogram_equalize(img):
    b, g, r = cv2.split(img)
    red = cv2.equalizeHist(r)
    green = cv2.equalizeHist(g)
    blue = cv2.equalizeHist(b)
    return cv2.merge((blue, green, red))

image = cv2.imread(args.imagePath)
# call equalize histogram function
equalized_histogram_image = histogram_equalize(image)

result = np.hstack((image,equalized_histogram_image)) #stacking images side-by-side
# show in output window
cv2.imshow("input-output",result);cv2.waitKey(0)
# write image
cv2.imwrite("out.jpg",equalized_histogram_image)