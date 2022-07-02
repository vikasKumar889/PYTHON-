import cv2

video = cv2.VideoCapture(0)

while True:
    state,img = video.read()
    h,w,_ = img.shape
    print(w,h)
    if state:
        cv2.rectangle(img,(0,h-6),(280,440),(0,255,0),-2)
        cv2.putText(img,'Webcam output',(10,h-10), cv2.FONT_HERSHEY_COMPLEX,1,(0,150,255),3)
    
        cv2.imshow('video output',img)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
video.release()
cv2.destroyAllWindows() 