#http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
#https://github.com/brendanwhitfield/python-OBD/wiki/OBD-Connections
import numpy as np
import cv2
import obd
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
#Connect to the car obd port
ports = obd.scanSerial()       # return list of valid USB or RF ports
print ports                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
connection = obd.OBD(ports[0]) # connect to the first port in the list
#Get current speed
speed=connection.commands['SPEED']
#Flag for if we need to be stopping!
flag=False
#Loop to process frames from running video device
while(ret):
  preSpeed=speed
  speed=connection.commands['SPEED']
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
#First figure out a better thresholding
#needs to be based off of a percentage of the last image
  if BlackRatio < (float(preRatio*.99)):
    print("Seeing red")
    if flag:
      if speed >=preSpeed :
        print ("Whoa dude, slow down")
      else:
        print ("Good job slowing down on the reds")
  else:
    print("No extra red in this frame!")
#Release the device at then end
cap.release()
