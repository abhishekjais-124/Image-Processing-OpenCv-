import numpy as np
import cv2


img = cv2.imread('lena.jpg',1) #first argument is image name,second is flag
print(img)                      #flag: 1 for colored, 0 for grey, -1 for normal with alpa channel

#to put text on image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'text',(10,500),font,4,(255,255,255),10,cv2.LINE_AA) #3rd is starting coordinates,4th is font faces,5th is font-size,6th is color,7th is thickness,8th is line type

cv2.imshow('image',img) #to show the image
cv2.waitKey(0) #to hold the image; 0 for always and other for time in milliseconds
cv2.destroyAllWindows()
