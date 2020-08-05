import cv2
import numpy as np
from matplotlib import pyplot as plt

#homogeneous filter- filter is homogeneous throughout

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #converting to rgb for the matplotlib

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel) #filter

blur = cv2.blur(img,(5,5)); #using blur method
#gaussian method - center has higher weight and side has lower weight
gblur = cv2.GaussianBlur(img,(5,5),0)
#median method - for salt-pepper noise . uses medians
median = cv2.medianBlur(img,5)
#bilateral - for keeping the edges sharp
bilateral = cv2.bilateralFilter(img,9,75,75)

titles = ['image','2D Convolution', 'blur', 'GaussianBlur','median','bilateral']
images = [img,dst,blur,gblur,median,bilateral]

for i in range(6):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]);plt.yticks([])

plt.show()