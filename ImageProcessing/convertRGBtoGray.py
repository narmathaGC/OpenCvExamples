### run code by using command "python convertRGBtoGray.py -p input.jpg"

import cv2
import numpy as np
import argparse

# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-p','--imagePath', help='mention rgb image absolute path')
args = parser.parse_args()


image = cv2.imread(args.imagePath)

# split rgb channel
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2] 
print type(red)

# convert RGB image to Gray
## without inbuild command
gray = np.uint8((0.2989*red) +  (0.5870*green) + (0.1140 *blue))
## using inbuild command
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show in output window
cv2.imshow("input-image",image)
cv2.imshow("gray-image",gray);cv2.waitKey(0)

# write image
cv2.imwrite("out.jpg",gray)
