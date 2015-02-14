#Import needed libraries
import numpy as np
import cv2

cap=cv2.VideoCapture(0)

i=0
ret=True
while(i<1):

  ret, frame =cap.read()
#  print("Camera is still running buddy") 
  cv2.imwrite('test{0}.png'.format(i), frame)
  i=i+1

cap.release()
cv2.destroyAllWindows()

