#Import needed libraries
import numpy as np
import cv2

def find_license(image):
  # convert the image to grayscale, blur it, and detect edges
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.bilateralFilter(gray, 11, 17, 17)
  edged = cv2.Canny(gray, 30, 200)
  cv2.imwrite('detect.png', edged) 
  # find the contours in the edged image and keep the largest one;
  # we'll assume that this is our piece of paper in the image
  (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
  # c = max(cnts, key = cv2.contourArea)
  # loop over our contours
  for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)
   # if len(approx) == 4:
    cv2.drawContours(image, [approx], -1, (0,255,0), 3)
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

# load the first image that contains an object that is KNOWN TO BE 6 feet
# from our camera, then find the license plate in the image, and initialize
# the focal length
image = cv2.imread('car.png')

#marker = find_license(image)
#focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

#print(focalLength)
# load the image, find the marker in the image, then compute the
# distance to the marker from the camera
#image = cv2.imread('car.png')
marker = find_license(image)
#inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
 
# draw a bounding box around the image and display it
#box = np.int0(cv2.cv.BoxPoints(marker))
#cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
#cv2.putText(image, "%.2fft" % (inches / 12),
#(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
#2.0, (0, 255, 0), 3)
cv2.imwrite("image.png", image)
#Set our capture object to dev0, assuming we only have one camera running
#cap=cv2.VideoCapture(0)
##Variables to stop our loop...in reality we want 
##this to run as long as the power is on
#i=0
#ret=True
##Loop to process frames from running video device
#while(ret):
# 
#  ret, frame =cap.read()
##  print("Camera is still running buddy")
##capture frame and write it to disk 
#  cv2.imwrite('test{0}.png'.format(i), frame)
#  i=i+1
##Release the device at then end
#cap.release()

