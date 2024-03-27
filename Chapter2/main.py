import cv2
import numpy as np

kernel = np.ones((3,3),np.int8)
img = cv2.imread("Resources/lena.png")
cv2.imshow("Image",img)

gray_img  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage",gray_img)

blur_img = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("BlurImage",blur_img)

canny_img = cv2.Canny(img,100,100)
cv2.imshow("CannyImage",canny_img)
# increase thickness of edges in canny by passing a matrix which is the kernel
img_dilation = cv2.dilate(canny_img,kernel,iterations=1)
cv2.imshow("DilationImage",img_dilation)

# opposite to dilation - making edges thinner
img_eroded = cv2.erode(img_dilation,kernel,iterations=1)
cv2.imshow("ErodedImage",img_eroded)

cv2.waitKey(0)