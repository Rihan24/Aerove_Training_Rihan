import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    edges = cv2.Canny(frame,100,200)
    #cv2.imshow(edges,cmap = 'gray')
    cv2.imshow('Input', edges)

    c = cv2.waitKey(1)
    if c == 27:    #press escape key to close window
        break

cap.release()
cv2.destroyAllWindows()