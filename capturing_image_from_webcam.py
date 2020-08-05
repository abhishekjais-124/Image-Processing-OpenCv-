import cv2
#capturing the livesstream frm camera or reading the video
"""
cap = cv2.VideoCapture(abc.mp4) #for the video in storage
cap = cv2.VideoCapture(0) # 0 or -1 for capturing the livesstream
"""
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #to get 4cc code
out = cv2.VideoWriter('outuput.avi',fourcc,20.0,(640,480)) #to record the video,first argument name of file, 2nd argument is 4cc code,3rd is frame per second,4th is the size of video

#to capture frame continuously

while True:
    if not cap.isOpened():  break   #function returns false if found error
    ret, frame = cap.read() #return True stored in ret if frame will be available
    if ret== True:
        #uncomment to change it to grey mode
        #grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);frame = grey
        #uncomment to get th width,height of the frame,and for other properties refer documentation
        #w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);h = cap.get(cv2.CAP_PROP_FRAME_WIDTH); print(w,h)

        out.write(frame) # to save in output file

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #if q key is pressed
            break
    else:
        break

cap.release() #release the resources
out.release()
cv2.destroyAllWindows()
