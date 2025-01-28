import numpy as np
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX

#Create a black image
img = cv2.imread('img.png',1)
cv2.putText(img , 'Ritika',(20,45),font,2,(0,200,140),5)

#Display the image
cv2.imshow('image',img)
cv2.waitKey()