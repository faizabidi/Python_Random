import numpy as np

x,y,z = raw_input("Please enter x, y, and z angles in degrees using commas. For example - \"45,60,90\"\n").split(',')

# Convert to radion
x = np.radians(int(x))
y = np.radians(int(y))
z = np.radians(int(z))


# Values in the rotation matrix
a = np.cos(y)*np.cos(z)
b = np.cos(x)*np.sin(z) + np.sin(x)*np.sin(y)*np.cos(z)
c = np.sin(x)*np.sin(z) - np.cos(x)*np.sin(y)*np.cos(z)
d = -np.cos(y)*np.sin(z)
e = np.cos(x)*np.cos(z) - np.sin(x)*np.sin(y)*np.sin(z)
f = np.sin(x)*np.cos(z) + np.cos(x)*np.sin(y)*np.sin(z)
g = np.sin(y)
h = -np.sin(x)*np.cos(y)
i = np.cos(x)*np.cos(y)

rotation_matrix = np.matrix('{} {} {}; {} {} {}; {} {} {}'.format(
	a, b, c, 
	d, e, f,
	g, h, i))

# Open the file
file = open("tc1.bin", "r")

# Extract binary data. dtype is uint32 because each part is a 32 bit integer
dt = np.dtype(int)
array = np.fromfile(file, dtype='uint32')

# Store in a list of lists
i = 1
j = 0
while i+3 < len(array):
	values = array[i:i+3]
	# Rotate these values using the rotation matrix
	values = np.dot(values, rotation_matrix)
	values = np.array(values)[0].tolist()
	#print(values[0])
	#x,y,y = values[0], values[1], values[2]
	# Convert it back to a list
	#list(np.array(values.reshape(-1,)))
	#values = ",".join(values).replace(",", " ")
	i += 3
	j += 1
	print (values)


# References:
# 1. https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions#Euler_angles_.28_z-y.E2.80.99-x.E2.80.B3_intrinsic.29_.E2.86.92_Rotation_matrix