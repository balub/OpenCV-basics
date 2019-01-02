import cv2
import numpy as np

cap = cv2.VideoCapture(0) #take input from webcam

while True:
    ret, frame = cap.read() # as long as ret is true read a frame from the captured image
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    #convert the rgb image captured above into grayscale 
    # cvtColor(img,conversion(cv2.COLOR_BGR2GRAY,cv2.COLOR_GRAY2BGR))
    cv2.imshow('frame',frame) #display the captured image frame
    cv2.imshow('Gray frame',gray) #display the gray scale image frame

    if cv2.waitKey(1) & 0xFF == ord('q') :  #if the key for 'q' is pressed exit the loop and stop the video capture
        break

cap.release() #stop capturng the video
cv2.destroyAllWindows() #close all open windows
