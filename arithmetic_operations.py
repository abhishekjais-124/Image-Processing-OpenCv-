import numpy as np
import cv2

img = cv2.imread('messi5.jpg')

print(img.shape)
print(img.size)
print(img.dtype) #prints datatype

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r)) #to merge bgr channels

#ROI of image or region of interest

#ex to copy the ball

ball = img[280:340, 330:390] #upper left and lower right
img[273:333, 100:160] = ball #placing the ball on the anther coordinate

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()