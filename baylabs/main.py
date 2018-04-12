# Run it with python3

import numpy as np
from matplotlib import pyplot as plt
from pylab import figure, axes, pie, title, show
from scipy.misc import toimage
import scipy
import scipy.misc as smp
from PIL import Image, ImageDraw, ImageFont

# Open the file
file = open("carotid.cine", "r")

# Extract binary data. dtype is uint8 because each part is an unsigned number between 0-255.
dt = np.dtype(int)
array = np.fromfile(file, dtype='uint8')
print("Total number of bytes in the file is %s" %len(array))

# We know that the first 1240 bytes are used for an "irrelevant header"
# Thus, let's ignore that and only have the relevant numbers in our array
array = array[1240:]
print("Bytes left after removing the header is %s" %len(array))

# Each frame has (241 * 1024 = 246784) numbers in it.
# There are a total of 32 frames. Thus, there would be 32 2d matrices

# Make a list of 32 arrays and then reshape them to matrices
all_frames = list()

print(len(array[0:246783]))

for i in range(0, len(array) - 1, 246784):
    frame = array[i:i + 246784]
    all_frames.append(frame)

# To represent it as a 2D image, it should be a matrix where rows = 241 and columns = 1024
i = 0
for matrices in all_frames:
    matrices.shape = (matrices.size//241, 241)
    #line1 = matrices[:,0]
    #print(type(line1))
    #print(line1)
    print(type(matrices))
    print(matrices.shape)
    print(matrices)
    column1 = matrices[:,[0]]
    column1 = column1.reshape((1, column1.size))
    #column1 = matrices[:,0]
    #column1.reshape((column1.size, 1))
    #data[:, [1, 9]]
    #column1.transpose()
    print(type(column1))
    #column1 = column1.reshape((1, column1.size()))
    print(column1.shape)
    print(column1)
    #break
    # Draw a line with this column
    toimage(column1).show()
    #break

    data = np.zeros( (1024,1024,1024), dtype=np.uint8)
    data[256, 256] = column1
    img = Image.fromarray(data, 'RGB')
    img.show()
    break
    #img = smp.toimage( data )       # Create a PIL image
    #img.save('frame1-new.png')

    #im = Image.open("frame1-new.png")

    #draw = ImageDraw.Draw(im)
    #draw.line((256, 256) + im.size, fill=column1)


    # write to stdout
    #im.save('frame1-new-modified.png')


    #break
    #print(matrices)
    toimage(matrices).show()
    break
    #toimage(column1).show()
    #break
    #scipy.misc.imsave('sci%s.png' %i, matrices)
    #break
    #img = Image.fromarray(matrices, 'RGB')
    #img.save('my.png')
    #img.show()
    #break;
    # Save as image
    #plt.imshow(matrices, interpolation='nearest')
    #plt.savefig('frame%s.png' %i)
    scipy.misc.imsave('frame%s.png' %i, matrices)
    i += 1

    