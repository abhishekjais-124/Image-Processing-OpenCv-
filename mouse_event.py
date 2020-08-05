import cv2
import numpy as np

#mouse events
#showing the coordinates on image after click
#callback function

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #if left button is clicked once
        print(x,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + " , " + str(y)
        cv2.putText(img,strxy,(x,y),font,0.5,(255,255,0),2)
        cv2.imshow('image',img) #showing on image the coordinates

    if event == cv2.EVENT_RBUTTONDOWN: #if right button of mouse is clicked
        blue = img[y,x,0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strbgr = str(blue) + " , " + str(green) + " , " + str(red)
        cv2.putText(img, strbgr, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)  # showing on image the, bgr channels


img = cv2.imread('lena.jpg')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
