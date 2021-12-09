import cv2

cap = cv2.VideoCapture("http://192.168.43.1:8080/video")

while(True):
    ret,frame=cap.read()
    cv2.imshow('video',frame)
    k=cv2.waitKey(1)
    if k==27:
        break

cap.release()