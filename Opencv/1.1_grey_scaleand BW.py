import cv2
import matplotlib.pyplot as plt

im_gray = cv2.imread('/home/rihan/Pictures/test2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('grey',cv2.WINDOW_NORMAL)
cv2.resizeWindow('grey', 600,600)

cv2.imshow('grey',im_gray)
cv2.waitKey(0)
#im_gray = cv2.medianBlur(im_gray,5)
#im_bw = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im_bw= cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#m_bw = cv2.threshold(im_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.namedWindow('bw',cv2.WINDOW_NORMAL)
cv2.resizeWindow('bw', 600,600)




cv2.imshow('bw',im_bw)

cv2.waitKey(0)
#cv2.imwrite('bw_image.jpg', im_bw)



