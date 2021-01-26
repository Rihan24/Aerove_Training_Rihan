def translate(img,M,rows,cols):
    dst = cv2.warpAffine(img,M,(cols,rows))
    plt.subplot(122),plt.imshow(dst),plt.title('translated')
    plt.show()

def rotate(img,M,rows,cols):
    dst = cv2.warpAffine(img,M,(cols,rows))
    plt.subplot(122),plt.imshow(dst),plt.title('rotated')
    plt.show()

def blur_img(blur):
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/rihan/Pictures/t_pic.png') 
rows,cols = img.shape[:2]

for i in range(0,4):
    M = np.float32([[1,0,100+i*10],[0,1,50+i*15]])
    translate(img,M,rows,cols)

for i in range(90,271,45):
    M = cv2.getRotationMatrix2D((cols/2,rows/2),i,1)
    rotate(img,M,rows,cols)

  
for i in range(5,7):
    blur = cv2.blur(img,(i,i))
    blur_img(blur)



cv2.destroyAllWindows()