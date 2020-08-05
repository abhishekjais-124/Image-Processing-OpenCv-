
import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 =cv2.imread('opencv-logo.png')

#making both images of same size

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
"""
#first method
dst = cv2.add(img,img2) #adding images
"""

#second method

dst = cv2.addWeighted(img,.8,img2,.2,0)

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()