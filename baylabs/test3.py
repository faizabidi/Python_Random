import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), np.uint8)

line = np.zeros((1, 100), dtype=np.uint8)
img = cv.line(img, (100,100), (300,300), line,4)

cv.imshow('Frame0', img)
cv.waitKey(0)