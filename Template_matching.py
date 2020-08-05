import cv2
import numpy as np
from matplotlib import pyplot as plt

#find the location of template in larger image

img = cv2.imread("messi5.jpg")
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg",0)
w,h = template.shape[::-1]


res =cv2.matchTemplate(grey_img,template,cv2.TM_CCOEFF_NORMED)
print(res)

#where there is match there is brightest point in matrix , value close to 1

threshold = 0.99; #decrease or increase it for accuracy
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
