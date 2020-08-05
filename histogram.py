import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# color intensity distribution idea

"""
#using matplotlib
img = cv.imread("lena.jpg")
#img = np.zeros((200,200),np.uint8)
#cv.rectangle(img,(0,100),(200,200),255,-1)
#cv.rectangle(img,(0,50),(100,100),127,-1)

b,g,r = cv.split(img)


cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)



plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()
"""
#another method
img = cv.imread("lena.jpg",0)
hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()