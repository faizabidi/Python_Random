lst = list()
d = dict()
#read file
inp = raw_input('Enter a file:')
try:
	if len(inp) < 1 : inp = 'mbox-short.txt'
	file = open(inp)
except:
	print 'File not found'
	exit()

#search in the file for the phrase 'From '
for i in file:
	if i.startswith('From '):
		i = i.split()
		
		#further divide the words to search for the hour separated by semi-colon
		i[5] = i[5].split(':')
		word = str(i[5][0])
	        #save in dictionary
		d[word] = d.get(word,0) + 1

#save dictionary in list
for key, value in d.items():
	lst.append( (key,value) )

#sort the list
lst.sort(reverse=False)

#print the values
for key, value in lst[:]:
	print key, value
