import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8) #black image
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread('opencv-logo.png')

# note black is termed as 0 and other are termed as 1
img1 = cv2.resize(img1,(500,500))
img2 = cv2.resize(img2,(500,500))

#bit = cv2.bitwise_and(img2,img1)
#bit = cv2.bitwise_or(img2,img1)
#bit = cv2.bitwise_xor(img2,img1)
bit = cv2.bitwise_not(img2,img1)


cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('bit',bit)

cv2.waitKey(0)
cv2.destroyAllWindows()