import numpy as np
import cv2

#first argument is list in which first is height, 2nd is width, 3rd is 3 always
#second is data type

img  = np.zeros([512,512,3],np.uint8) #forms black image


cv2.imshow('image',img) #to show the image
cv2.waitKey(0) #to hold the image; 0 for always and other for time in milliseconds
cv2.destroyAllWindows()
