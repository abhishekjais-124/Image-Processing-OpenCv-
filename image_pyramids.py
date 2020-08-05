import cv2
import numpy as np
from matplotlib import pyplot as plt

#a multi scale representation in which a signal or an image is subject to repeated smoothing and subsampling


img = cv2.imread("lena.jpg")

#gaussain pyramid
lr1 = cv2.pyrDown(img) #decresing the resolution
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2) #increasing the resolution

cv2.imshow("Original",img)
cv2.imshow("pyrdown 1",lr1)
cv2.imshow("pyrdown 2",lr2)
cv2.imshow("pyrup 1",hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()


