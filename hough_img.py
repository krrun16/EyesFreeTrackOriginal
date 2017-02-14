#!/usr/bin/env python
#I GOT THIS CODE FROM http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html AND http://stackoverflow.com/questions/33541551/hough-lines-in-opencv-python AND http://stackoverflow.com/questions/4195453/how-to-resize-an-image-with-opencv2-0-and-python2-6

import cv2
import numpy as np
import argparse

def slope ():
    print((y2*1.0-y1*1.0)/(x2*1.0-x1*1.0))
    return (y2*1.0-y1*1.0)/(x2*1.0-x1*1.0)

def interpolate(height, width):
    xtop = x2*1.0 - (y2*1.0/slope())
    xbottom = x1*1.0 - ((y1*1.0 - height)/slope())
    if (xtop == float("inf") or xbottom == float("inf")):
        yleft = y1-(x1*slope())
        yright = y2+slope()*(width-x2)
        return width, 0, int(yleft), int(yright)
    else:
        print ("xtop = " + str(xtop))
        print ("xbottom = " + str(xbottom))
        return int(xtop), int(xbottom), height, 0

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

src = cv2.imread(args["image"])

height, width = src.shape[:2]
SCALE = 1
height = int(SCALE*height)
width = int(SCALE*width)

img = cv2.resize(src, (int(width), int(height)), interpolation = cv2.INTER_AREA)

boundaries = [
    ([17, 15, 70], [60, 70, 255]),
    ([150, 150, 200], [255, 255, 255])
    #([82, 90, 141], [255, 255, 255])
]

#Red detection: [17, 15, 70], [60, 70, 255]
#White detection: [82, 90, 141], [255, 255, 255]

#Red
redlower = np.array(boundaries[0][0], dtype = "uint8")
redupper = np.array(boundaries[0][1], dtype = "uint8")

redmask = cv2.inRange(img, redlower, redupper)
redoutput = cv2.bitwise_and(img, img, mask = redmask)

#White
whitelower = np.array(boundaries[1][0], dtype = "uint8")
whiteupper = np.array(boundaries[1][1], dtype = "uint8")

whitemask = cv2.inRange(img, whitelower, whiteupper)
whiteoutput = cv2.bitwise_and(img, img, mask = whitemask)

output = cv2.addWeighted(redoutput,0.5,whiteoutput,0.5,0)

cv2.imshow('output',output)
cv2.waitKey(0)

blur = cv2.GaussianBlur(output,(3,3), 0)

gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

cv2.imshow('edges',edges)
cv2.waitKey(0)

minLineLength=30
maxLineGap=10
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        print(lines[x])
        slp = slope()
        cv2.line(output,(x1,y1),(x2,y2),(255,0,0),2)
        if slp<=0:
            if slp>=-.1:
                xtop, xbottom, yleft, yright = interpolate(height, width)
                cv2.line(output,(xbottom,yleft),(xtop,yright),(0,255,0),2)
            elif slp>=-.2:
                xtop, xbottom, yleft, yright = interpolate(height, width)
                cv2.line(output,(xbottom,yleft),(xtop,yright),(255,255,0),2)
            elif slp>=-.3:
                xtop, xbottom, yleft, yright = interpolate(height, width)
                cv2.line(output,(xbottom,yleft),(xtop,yright),(0,255,255),2)
            elif slp>=-.4:
                xtop, xbottom, yleft, yright = interpolate(height, width)
                cv2.line(output,(xbottom,yleft),(xtop,yright),(0,0,255),2)
            elif slp>=-.5:
                xtop, xbottom, yleft, yright = interpolate(height, width)
                cv2.line(output,(xbottom,yleft),(xtop,yright),(128,128,0),2)
            elif slp>=-.6:
                xtop, xbottom, yleft, yright = interpolate(height, width)
                cv2.line(output,(xbottom,yleft),(xtop,yright),(0,128,128),2)
            else:
                xtop, xbottom, yleft, yright = interpolate(height, width)
                cv2.line(output,(xbottom,yleft),(xtop,yright),(255,0,255),2)
        else:
            xtop, xbottom, yleft, yright = interpolate(height, width)
            cv2.line(output,(xbottom,yleft),(xtop,yright),(255,0,0),2)

cv2.imshow('hough',output)
cv2.waitKey(0)



