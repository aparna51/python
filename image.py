#!/usr/bin/python

import cv2
img=cv2.imread('index.jpeg',1)
cv2.line(img,(0,0),(100,180),(0,255,0),5)
cv2.imshow('pic',img)
print("yeah")
cv2.waitKey(0)
cv2.destroyWindow('pic')

