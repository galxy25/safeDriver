#http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
import numpy as np
import cv2
#import os
#Function to compute the ratio of black pixels to non black pixels
def countBlackPixels(grayImg):
  height=grayImg.shape[0]
  width=grayImg.shape[1]
  size = width * height
  return (size - cv2.countNonZero(grayImg)) / float(size)
# define rgb range for red colors
red = [[17, 15, 100], [50, 56, 200]]
# create NumPy arrays from the boundaries
lower = np.array(red[0], dtype = "uint8")
upper = np.array(red[1], dtype = "uint8")
#Set our capture object to dev0, assuming we only have one camera running
cap=cv2.VideoCapture(0)
#set width and height so we reduce our image size
cap.set(4,320)
cap.set(5,240)
#Variables to stop our loop...in reality we want
#this to run as long as the power is on
ret=True
BlackRatio=1.0
#Loop to process frames from running video device
while(ret):
  preRatio=BlackRatio
#Capture the image from our device
  ret, image =cap.read()
# find the colors within the specified boundaries and apply
# the mask
  mask = cv2.inRange(image, lower, upper)
  output = cv2.bitwise_and(image, image, mask = mask)
#Convert the image to gray scale so we can count number of non black pixels
  gray=cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
#Count the number of non black pixels
  BlackRatio=countBlackPixels(gray)
#First figure out
  if BlackRatio > preRatio:
    print (BlackRatio)
  else:
    print("No extra red in this frame!")
#Release the device at then end
cap.release()
