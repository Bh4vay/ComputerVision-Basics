import cv2


# image reading
img = cv2.imread("Resources/lena.png")
cv2.imshow("Image",img)


# video capture
cap = cv2.VideoCapture(0)
# id = 3 for setting width
cap.set(3,400)
#  id = 4 for setting height
cap.set(4,400)
while True:
    # capturing each frame from webcam
    ret, frame = cap.read()
    cv2.imshow("Webcam",frame)
    # closing the webcam by pressing a key
    if cv2.waitKey(1) & 0xFF == ord('x'):        
        break
    
    
cap1 = cv2.VideoCapture("Resources/test.mp4")
cap1.set(3,400)
cap1.set(4,400)
while True:
    ret, frame1 = cap1.read()
    cv2.imshow("Video",frame1)
    # closing the webcam by pressing a key
    if cv2.waitKey(1) & 0xFF == ord('c'):        
        break
    
cv2.waitKey(0)