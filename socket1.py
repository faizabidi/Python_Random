#module to retrieve data over sockets
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#port 80 is for http
mysock.connect(('www.py4inf.com', 80))
#the two newlines at the end only separates the header files and the actual body content we'll get
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
	#receive 512 characters of data at a time
	data = mysock.recv(512)
	#when all data is send, get out of printing loop
	if (len(data) < 1):
		break
	print data;
	
mysock.close()