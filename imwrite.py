import cv2

img = cv2.imread('img.png',0)
print(img)

status = cv2.imwrite('china.png',img)
print("Image written to file-system : ",status)
