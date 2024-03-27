import cv2
import numpy as np
img = np.zeros((300,300,3))

cv2.line(img,(0,0),(300,300),(255,0,0),2)
cv2.rectangle(img,(0,0),(250,250),(0,0,255))
cv2.circle(img,(100,100),30,(255,255,0),5)
cv2.putText(img,"IMAGE",(150,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(230,210,255),1)

cv2.imshow("Image",img)
cv2.waitKey(0)