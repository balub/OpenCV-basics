import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img1.jpg',cv2.IMREAD_GRAYSCALE) 
#  creates a img variable using imread() function takes in 2 inputs file name and the filter
#  that is being applied IMREAD_GRAYSCALE or IMREAD_COLOR

cv2.imshow('Image',img) # used to display a image imshow(name of window, img name)
cv2.waitKey(0) #used to close window in press of any button
cv2.destroyAllWindows() #closes all open windows 