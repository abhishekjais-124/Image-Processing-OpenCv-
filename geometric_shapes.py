import numpy as np
import cv2


img = cv2.imread('lena.jpg',1) #first argument is image name,second is flag
print(img)                      #flag: 1 for colored, 0 for grey, -1 for normal with alpa channel

#to draw a line
img = cv2.line(img,(0,0),(255,255),(0,0,255),5)  #first is image, 2nd is begin coordinates,3rd is end coordinates, 4th is color in bgr(reverse of rgb) format,5th is thickness
#to draw arrowed line
img = cv2.arrowedLine(img,(0,0),(225,275),(255,0,255),5)
#to draw rectangle
img = cv2.rectangle(img,(384,0),(510,128),(255,0,0),5)  #firs image, 2nd is upper left coordinates,3rd is lower right, 4th is color, 5th is thickness
#to draw rectangle filled with color
img = cv2.rectangle(img,(384,400),(310,428),(255,0,0),-1) #last parameter is -1
#to draw circle
img = cv2.circle(img,(447,63),63,(0,255,0),-1) #first is image, 2nd is center, 3rd is radius,4th is color,5 th is thickness(>0 for thickness,-1 to fill all)


cv2.imshow('image',img) #to show the image
cv2.waitKey(0) #to hold the image; 0 for always and other for time in milliseconds
cv2.destroyAllWindows()
