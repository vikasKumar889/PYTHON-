import cv2

video = cv2.VideoCapture(0)

while True:
    state,img = video.read()
    if state:
        cv2.rectangle(img,(0,0),(280,40),(0,255,0),-1)
        cv2.putText(img,'Webcam output',(10,30), cv2.FONT_HERSHEY_COMPLEX,1,(0,150,255),2)
    
        cv2.imshow('video output',img)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
video.release()
cv2.destroyAllWindows() 