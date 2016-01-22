d = dict()
lst = list()
#read a file
inp = raw_input('Enter a file:')
try:
	if len(inp) < 1 : inp = 'romeo.txt'
	file = open(inp)
except:
	print 'File not found'
	exit()

#create a list of words from the file and then a dictionary
for i in file:
	#create a list of each line separated by white spaces
	i = i.split()
	#iterare through the first line and save in the dictionary
	for words in i:
		d[words] = d.get(words,0) + 1

#one method		
#reverse the dictionary in terms of key and value and save in a list
for key,value in d.items():
	lst.append((value,key))

lst.sort(reverse=True)

#print the top ten values
for value,key in lst[:10]:
	print key,value

"""#second method
print sorted( [(v,k) for k,v in d.items()] )"""
