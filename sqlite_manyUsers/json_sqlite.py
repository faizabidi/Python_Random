import json
import sqlite3

#create a DB
conn = sqlite3.connect('ManyStudents.sqlite')

#lke a file handler to fetch results
cur = conn.cursor()

#drop tables if already exists
#create tables
cur.executescript ('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Course;
	DROP TABLE IF EXISTS Member;

	CREATE TABLE User (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT);

	CREATE TABLE Course (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title TEXT);

	CREATE TABLE Member (
		user_id INTEGER,
		course_id INTEGER,
		role INTEGER,
		PRIMARY KEY (user_id, course_id));
''')

#input file name from user
fname = raw_input('Enter file name:')

try:
	if len(fname) < 1 : fname = 'roster_data.json'
except:
	print 'File not found!'

#file handler to open and read the json file
data = open(fname).read()

#type of jsonData would be a dictionary
jsonData = json.loads(data)

#to print the json file, uncomment below line
#print json.dumps(jsonData, indent = 4)

#print jsonData[0][0];
for items in jsonData:
#	print items;
	user_name = items[0]
	course_title = items[1]
	member_role =  items[2]

	print user_name, course_title, member_role

	cur.execute('''INSERT OR IGNORE INTO User (name) 
		VALUES ( ? )''', (user_name, ));
	#select the first row and save the id in user_id
	cur.execute('SELECT id from User WHERE name = ( ? )''', (user_name, ))
	user_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Course (title) 
		VALUES ( ? )''', (course_title, ));
	#select the first row and save the id in course_id
	cur.execute('SELECT id from Course WHERE title = ( ? )''', (course_title, ))
	course_id = cur.fetchone()[0]	

	cur.execute('''INSERT or IGNORE INTO Member (user_id, course_id, role) 
		VALUES ( ?, ?, ? )''', (user_id, course_id, member_role ));
	#select the first row and save the id in user_id
	cur.execute('SELECT id from User WHERE name = ( ? )''', (user_name, ))

	#commit the changes
	conn.commit()