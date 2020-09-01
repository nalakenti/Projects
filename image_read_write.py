import cv2
img=cv2.imread('image.jpeg',-1)
print(img)
cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('cpy_image.jpeg',img)