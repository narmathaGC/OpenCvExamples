### run code by using command "python frameToVideoConvertor.py -f frames/"

import cv2
import glob,os
import numpy as np
import argparse

# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-f','--folderPath', help='mention folder path that contains frame')
args = parser.parse_args()


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
flag = 0

for frame in glob.glob(args.folderPath + os.path.sep +'*'):
	im = cv2.imread(frame)
	if flag == 0 :
		out_write= cv2.VideoWriter('out.mp4',fourcc, 30.0, tuple(im.shape[:2][::-1]))
		flag = 1
	out_write.write(im)
out_write.release()