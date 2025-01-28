import numpy as np
import cv2
img = cv2.imread('people1.png',1)

#CIRCLE
cv2.circle(img , (80,80), 55 ,(0,255,0),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#RECTANGLE
cv2.rectangle(img,(159,25),(200,150),(0,255,255),5)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()

#ELLIPSE
cv2.ellipse(img, (150,50), (80,20), 5, 0, 360, (0,0,255),-1)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()

#LINE
cv2.line(img , (10,0) ,(150,150),(0,0,0),15)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
