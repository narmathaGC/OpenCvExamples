### run code by using command "python templateMatching.py -i input_image.jpg -t template_image.jpg"

import cv2
import numpy as np
import argparse

# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-i','--imagePath', help='mention image absolute path')
parser.add_argument('-t','--templateImagePath', help='mention template image absolute path')

args = parser.parse_args()



image = cv2.imread(args.imagePath)

# Convert it to grayscale
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Read the template
template = cv2.imread(args.templateImagePath,0)
 
# Store width and heigth of template in w and h
w, h = template.shape[::-1]
 
# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
 
# Specify a threshold
threshold = 0.8
 
# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold) 
 
# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
 

# show in output window
cv2.imshow("input-image",image);cv2.waitKey(0)
# write image
cv2.imwrite("out.jpg",image)

### referred http://www.geeksforgeeks.org/template-matching-using-opencv-in-python/ 
