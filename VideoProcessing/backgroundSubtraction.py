### run code by using command "python backgroundSubtraction.py -v  videoname.mp4"
# BackgroundSubtractorMOG2 selects the appropriate number of gaussian distribution for each pixel. It provides better adaptibility to varying scenes due illumination changes etc
# An option of selecting whether shadow to be detected or not is present. If detectShadows = True (which is so by default), it detects and marks shadows, but decreases the speed. 
# Shadows will be marked in gray color.

import cv2
import os
import argparse
import numpy as np
import cv2



# get input from terminal
parser = argparse.ArgumentParser()
parser.add_argument('-v','--videoPath', help='mention video absolute path')
args = parser.parse_args()



def backgroundSubtraction(videoPath):
    cap = cv2.VideoCapture(videoPath)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*"MJPG") 
    video = cv2.VideoWriter('BgSub-Output.mp4', fourcc, 30.0,size)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    
    while(1):
        ret, frame = cap.read()
        if ret == True:
            fgmask = fgbg.apply(frame)
            video.write(fgmask)
        else:
            break

    cap.release()
    video.release()
    cv2.destroyAllWindows()

backgroundSubtraction(args.videoPath)
