import cv2
import numpy as np
img = cv2.imread("Resources/lena.png")

# horizontal stack - join images
hor = np.hstack((img,img))
# vertical stack
ver = np.vstack((img,img))

cv2.imshow("Image",hor)
cv2.imshow("Image",ver)
cv2.waitKey(0)