import cv2
img=cv2.imread('image.jpeg',1)
img=cv2.line(img,(0,0),(255,255),(20,186,252),10)
img=cv2.arrowedLine(img,(0,255),(255,255),(3,186,252),10)
img=cv2.rectangle(img, (384,0), (510,128), (0,0,255), -1)
cv2.imshow('image',img)

cv2.waitKey(5000)



cv2.destroyAllWindows()
