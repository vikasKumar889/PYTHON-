import cv2

im = cv2.imread('20190625_191425.jpg')
print(im.shape)
cv2.imshow('Image window', im)
cv2.waitKey(0)