### run code by using command "python videoToFrameConvertor.py -v  videoname.mp4"

import cv2
import os
import argparse


# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-v','--videoPath', help='mention video absolute path')
args = parser.parse_args()


def convertVideoToFrame(videoPath):
	cap = cv2.VideoCapture(videoPath)
  	os.system('mkdir videoToFrames')
	i=0
	while(cap.isOpened()):
	    # Capture frame-by-frame
	    ret, frame = cap.read()
	    if ret == True:
	    	path = 'videoToFrames/'+ videoPath.split('/')[-1].split('.')[0] + '_' +str(i) +'.jpg'
	    	cv2.imwrite(path,frame)
	    	i=i+1
	    else:
	    	break

	# When everything done, release the capture
	cap.release()

convertVideoToFrame(args.videoPath)