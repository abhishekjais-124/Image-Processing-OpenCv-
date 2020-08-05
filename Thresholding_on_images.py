import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#thresholding is used for separating object frm background

img = cv.imread("gradient.png",0)
_, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY) #if value of pixel is less than 127 then it ts categorised to one block else categorised to another
_, th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)#inverse of above
_, th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC) #pixel will not change upto 127 then it remains until the end
_, th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO) #pixel will be 0 upto 127 and then remain unchanged
_, th5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV) #inverse of above

#to show normally
"""
cv.imshow("Image",img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()
"""

#To show using matplotlib

titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]);plt.yticks([])

plt.show()