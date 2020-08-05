import cv2

img = cv2.imread('lena.jpg',-1) #first argument is image name,second is flag
print(img)                      #flag: 1 for colored, 0 for grey, -1 for normal with alpa channel

cv2.imshow('image',img) #to show the image
k = cv2.waitKey(0) & 0xFF #to hold the image; 0 for always and other for time in milliseconds, 0xFF is for 64-bit machines

if k==27:   #esc is pressed
    cv2.destroyAllWindows() #destroy the window
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img) #save the file with different name
    cv2.destroyAllWindows()
