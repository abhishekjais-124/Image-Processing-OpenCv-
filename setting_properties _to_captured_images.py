import cv2
#capturing the livesstream frm camera or reading the video
"""
cap = cv2.VideoCapture(abc.mp4) #for the video in storage
cap = cv2.VideoCapture(0) # 0 or -1 for capturing the livesstream from default device
"""
cap = cv2.VideoCapture(0)

# note if resolution is not available then it will take the available resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080) #to change width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720) #to change height


"""
we can also write above as
cap.set(3,1080)
cap.set(4,720)
"""
print(cap.get(3))
print(cap.get(4))

#to capture frame continuously

while True:
    if not cap.isOpened():  break   #function returns false if found error
    ret, frame = cap.read() #return True stored in ret if frame will be available
    #uncomment to change it to grey mode
    #grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);frame = grey
    #uncomment to get th width,height of the frame,and for other properties refer documentation
    #w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);h = cap.get(cv2.CAP_PROP_FRAME_WIDTH); print(w,h)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #if q key is pressed
        break

cap.release() #release the resources
cv2.destroyAllWindows()
