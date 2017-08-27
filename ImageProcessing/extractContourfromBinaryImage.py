### run code by using command "python extractContourfromBinaryImage.py -p input.jpg"

import cv2
import numpy as np
import argparse

# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-p','--imagePath', help='mention binary image absolute path')
args = parser.parse_args()


image = cv2.imread(args.imagePath)
inputImage = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel, iterations=1)

##### simple contour Extraction #####

edgeImage = thresh - erosion
result = np.hstack((thresh,edgeImage)) #stacking images side-by-side
cv2.imshow("input-output",result);cv2.waitKey()
cv2.imwrite("contour_output_using _morph.png",edgeImage)


#### using find contours ####

    # find contours arguments first one is source image, second is contour retrieval mode, third is contour approximation method
    # RETR_EXTERNAL it returns only extreme outer 
    # RETR_TREE retrieves all the contours and creates a full family hierarchy list.
    # CHAIN_APPROX_NONE gives all contours in a region, CHAIN_APPROX_SIMPLE removes all redundant points and compresses the contour, thereby saving memory.

_, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours[:]:
        # first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness
        cv2.drawContours(image, [cnt], -1, (0,255,0), 2)

# find the biggest area
maxSizeObject = max(contours[:], key = cv2.contourArea)
cv2.drawContours(image, [maxSizeObject], 0, (0,0,255), 2)
result = np.hstack((inputImage,image))
# show in output window
cv2.imshow("input-output",result);cv2.waitKey(0)
# write image
cv2.imwrite("output_findcontours.jpg",image)