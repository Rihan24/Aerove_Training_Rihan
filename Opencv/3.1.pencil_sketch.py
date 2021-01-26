import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/rihan/Pictures/test2.jpg',0)

edges = cv2.Canny(img,100,200)


plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('pencil_sketch'), plt.xticks([]), plt.yticks([])

plt.show()