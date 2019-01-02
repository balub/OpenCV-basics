import cv2
import numpy as np

cap = cv2.VideoCapture(0) #take input from webcam

while True:
    ret, frame = cap.read() # as long as ret is true read a frame from the captured image
    cv2.imshow('frame',frame) #display the captured image frame

    if cv2.waitKey(1) & 0xFF == ord('q') :  #if the key for 'q' is pressed exit the loop and stop the video capture
        break

cap.release() #stop capturng the video
cv2.destroyAllWindows() #close all open windows
