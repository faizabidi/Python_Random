import urllib
from BeautifulSoup import *

inp_url = raw_input('Enter web address:')

#position of the hyperlink from the top
inp_position = int(raw_input('Enter position:'))

#number of times the links need to be surfed
inp_count = int(raw_input('Enter count:'))

#loop to parse links depending on the inp_count given by user
for i in range(inp_count):
	#read the first link first
	fhand = urllib.urlopen(inp_url).read()
	
	print 'Retrieving link',i,':',inp_url
	
	#soupify the html received
	soup = BeautifulSoup(fhand)
	
	#find the list of anchor tags and parse the href content in them so that we... 
	#...can parse the next link
	tags = soup('a') #tags will be a list
	
	#get the href part of the anchor tag along with the contents
	inp_url = tags[inp_position-1].get('href')
	inp_content = tags[inp_position-1].contents[0]
	
#print the last value stored in inp_content, which is our required value
print 'Last url parsed was:',inp_url
print 'The content in the last url was:',inp_content