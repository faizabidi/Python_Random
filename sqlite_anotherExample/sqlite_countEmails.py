import sqlite3
import re

#create a db to store data
conn = sqlite3.connect('organizationCount.sqlite')

#used to manage the context of a fetch operation
cur = conn.cursor()

#drop table if already exists
cur.execute('''
	DROP TABLE IF EXISTS Counts''')

#create rows in the table
cur.execute('''
	CREATE TABLE Counts (org TEXT, count INTEGER)''')

#input file name from user
inp = raw_input('Enter file name:')
if len(inp) < 1 : inp = 'mbox.txt'

#open the file
fh = open(inp)

for line in fh:
	#serach for a pattern in the file
	if not line.startswith('From:') : continue
	
	#split and form a list based on spaces
	line = line.split()

	#split the email by the '@' sign
	email = line[1].split('@')

	#email is the second element of the "email" list
	domain = email[1]


	#can also use regular expressions to find the domain. But the...
	#..below code rerun a list of domains.
	'''line = line.strip()
	domain = re.findall('@([^ ]*)',line)
	print domain'''

	#print domain
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain, ))

	try:
		#if organization found in the DB, add count value by 1. fetchone()[0] fetches...
		#...the count value found in the previous SQL statment.
		cur.fetchone()[0]
		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ? ',(domain, ))
	except:
		#if organization is not found in the DB, insert a record
		cur.execute('''INSERT INTO Counts (org,count) VALUES(?,1)''',(domain, ))

	#commit the data into drive memory
	conn.commit()

sqlstr = 'SELECT * FROM Counts ORDER BY count DESC Limit 20'

#just to check and print on the terminal
for row in cur.execute(sqlstr):
	print str(row[0]),row[1]

#close the cursor
cur.close()