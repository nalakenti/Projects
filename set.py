import  cv2
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,700)
cap.set(4,700)
print(cap.get(3))
print((cap.get(4)))


while(True):
    ret,frame=cap.read()
    if ret==True:

        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break



cap.release()

cv2.destroyAllWindows()