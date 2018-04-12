import numpy as np
import scipy.misc as smp
from PIL import Image, ImageDraw

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros((512,512,3), dtype=np.uint8)

#data[512,512] = [254,0,0]       # Makes the middle pixel red
#data[512,513] = [0,0,255]       # Makes the next pixel blue

img = smp.toimage( data )       # Create a PIL image
#img.show()  
img.save('my.png')

im = Image.open("my.png")

draw = ImageDraw.Draw(im)
draw.line((256, 256) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)

# write to stdout
im.save('my2.png')
im.show()