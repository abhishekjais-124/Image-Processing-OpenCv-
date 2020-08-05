import cv2
import numpy as np

#mouse events
#after every click i draw a point and then connect points using line

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #if left button is clicked once
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage = np.zeros((512,512,3),np.uint8) #new window
        mycolorImage[:] = (blue,green,red) #changing color of new window

        cv2.imshow('colorwindow',mycolorImage) #showing on image



img = cv2.imread('lena.jpg')
#img = np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
