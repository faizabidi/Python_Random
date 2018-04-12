import numpy as np
from scipy import misc
from scipy.interpolate import interp2d
from math import pi, atan2, hypot

inputImagePath = 'frame0.png'
resultWidth = 800
resultHeight = 600
centerX = resultWidth / 2
centerY = - 50.0
maxAngle =  45.0 / 2 / 180 * pi
minAngle = -maxAngle
minRadius = 100.0
maxRadius = 600.0

inputImage = misc.imread(inputImagePath)
inputImage = inputImage.reshape((1024, 241, 1))
print(inputImage.shape)


h,w,chn = inputImage.shape
print(f"h = {h} w = {w} chn = {chn}")
channels = [inputImage[:,:,i] for i in range(3)]
interpolated = [interp2d(range(w), range(h), c) for c in channels]
resultImage = np.zeros([resultHeight, resultWidth, 3], dtype = np.uint8)

for c in range(resultWidth):
  for r in range(resultHeight):
    dx = c - centerX
    dy = r - centerY
    angle = atan2(dx, dy) # yes, dx, dy in this case!
    if angle < maxAngle and angle > minAngle:
      origCol = (angle - minAngle) / (maxAngle - minAngle) * w
      radius = hypot(dx, dy)
      if radius > minRadius and radius < maxRadius:
        origRow = (radius - minRadius) / (maxRadius - minRadius) * h
        for chn in range(3):
          resultImage[r, c, chn] = interpolated[chn](origCol, origRow)

import matplotlib.pyplot as plt
plt.imshow(resultImage)
plt.show()