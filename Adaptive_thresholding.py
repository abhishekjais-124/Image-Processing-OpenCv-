import cv2 as cv
import numpy as np

#adaptive thresholding is used for varying illumination

img = cv.imread("sudoku.png",0)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("Image",img)
cv.imshow("th2",th2)
cv.imshow("th3",th3)

cv.waitKey(0)
cv.destroyAllWindows()