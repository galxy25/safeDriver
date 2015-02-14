#Import needed libraries
import numpy as np
import cv2

def find_licence(image):
  # convert the image to grayscale, blur it, and detect edges
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (5, 5), 0)
  edged = cv2.Canny(gray, 35, 125)
 
  # find the contours in the edged image and keep the largest one;
  # we'll assume that this is our piece of paper in the image
  (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  c = max(cnts, key = cv2.contourArea)
 
  # compute the bounding box of the of the paper region and return it
  return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
  # compute and return the distance from the maker to the camera
  return (knownWidth * focalLength) / perWidth
 
# initialize the known distance from the camera to the object, which
# in this case is 24 inches
KNOWN_DISTANCE = 72.0
 
# initialize the known object width, which in this case, the piece of
# paper is 11 inches wide
KNOWN_WIDTH = 12.0
 
# initialize the list of images that we'll be using
IMAGE_PATHS = ["IMG_020.JPG"]
 
# load the first image that contains an object that is KNOWN TO BE 6 feet
# from our camera, then find the license plate in the image, and initialize
# the focal length
image = cv2.imread(IMAGE_PATHS[0])
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

print(focalLength)
#Set our capture object to dev0, assuming we only have one camera running
cap=cv2.VideoCapture(0)
#Variables to stop our loop...in reality we want 
#this to run as long as the power is on
i=0
ret=True
#Loop to process frames from running video device
while(i<1):
 
  ret, frame =cap.read()
#  print("Camera is still running buddy")
#capture frame and write it to disk 
  cv2.imwrite('test{0}.png'.format(i), frame)
  i=i+1
#Release the device at then end
cap.release()

