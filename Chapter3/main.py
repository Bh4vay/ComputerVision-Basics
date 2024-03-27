import cv2


# image reading
img = cv2.imread("Resources/lambo.png")
print(img.shape)

# resize
img_resize = cv2.resize(img,(300,200))

# cropped - height then width
img_crop = img[0:200,200:500]

 
cv2.imshow("ImageRe",img_resize)
cv2.imshow("ImageCrop",img_crop)
cv2.imshow("Image",img)
cv2.waitKey(0)