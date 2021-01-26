import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('/home/rihan/Pictures/test3.jpg',)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2BGB)

plt.imshow(image)
plt.show()