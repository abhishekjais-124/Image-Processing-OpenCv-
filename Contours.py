import cv2
import numpy as np
from matplotlib import pyplot as plt

#curves joining all cotinuous points along the boundary which all have same color or intensity

img =cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#appplying threshold

ret,thresh  = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("No of Contours = ",len(contours))

# to draw boundary of all
cv2.drawContours(img,contours,-1,(0,255,0),3)

#to draw single contours
"""
cv2.drawContours(img,contours,1,(0,255,0),3)
cv2.drawContours(img,contours,2,(0,255,0),3)
cv2.drawContours(img,contours,3,(0,255,0),3)
"""

cv2.imshow("Image",img)
cv2.imshow("Image gray",imgray)


cv2.waitKey(0)
cv2.destroyAllWindows()
