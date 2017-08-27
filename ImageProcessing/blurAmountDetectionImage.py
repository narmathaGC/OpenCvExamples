### run code by using command "python blurAmountDetectionImage.py -p input.jpg"

import cv2
import numpy as np
import argparse

# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-p','--imagePath', help='mention rgb image absolute path')
args = parser.parse_args()


image = cv2.imread(args.imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
variance = cv2.Laplacian(gray, cv2.CV_64F).var()

# if variance of Laplacian is higher then the image is not blurry (i.e, more number of edges found in the image) anf if variance is lesser then the image is considered blurry, 
# threshold value is set such a way that it correctly classifies blurry and non-blurry images 

if variance < 200:   #--- threshold value is set based on user preferences
	print "Image is Blurry"
 
cv2.putText(image, "Blurry Amount : " + str(variance) , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

# show the image
cv2.imshow("input-image",image);cv2.waitKey(0)
