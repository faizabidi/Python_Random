#use file Library.xml to test

import sqlite3
#to read XML data, import the XML module
import xml.etree.ElementTree as ET

#create a DB to store data
conn = sqlite3.connect('musicaldata.sqlite')

#cursor to fetch results
cur = conn.cursor()

#use executescript() to run several queries together
cur.executescript ('''
	DROP TABLE IF EXISTS Artist;
	DROP TABLE IF EXISTS Genre;
	DROP TABLE IF EXISTS Album;
	DROP TABLE IF EXISTS Track;

	CREATE TABLE Artist (
    	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    	name    TEXT UNIQUE);

	CREATE TABLE Genre (
   		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   	 	name    TEXT UNIQUE);

	CREATE TABLE Album (
   		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   	 	artist_id  INTEGER,
   	 	title   TEXT UNIQUE);

	CREATE TABLE Track (
   		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    	title TEXT  UNIQUE,
    	album_id  INTEGER,
    	genre_id  INTEGER,
    	len INTEGER, rating INTEGER, count INTEGER);
''')

#input file name from user
fname = raw_input('Enter filename:')

try:
	if len(fname) < 1: fname = 'Library.xml'
except:
	print 'File not found!'
	exit()

#function to find the needed information within tags
def lookup(d, attrib):	
	found = False
	for child in d:
		if found: return child.text
		#look for the "key" tag in the file and then compare the text in it
		if (child.tag == 'key' and child.text == attrib):
			found = True
	#return None if not found
	return None

#process the xml file
tree = ET.parse(fname)

#find all data in the dict tag
stuff = tree.findall('dict/dict/dict')

#print number of tag count
print 'Dict tag cout =', len(stuff)

for item in stuff:
	
	#check and skip if tag is empty
	if (lookup(item, 'Track ID') is None) : continue

	track_title = lookup(item,'Name')
	track_length = lookup(item,'Total Time')
	track_rating = lookup(item,'Rating')
	track_count = lookup(item,'Track Count')

	artist_name = lookup(item,'Artist')

	genre_name = lookup(item,'Genre')

	album_title = lookup(item,'Album')

	#skip records if missing info
	if track_title is None or artist_name is None or album_title is None or genre_name is None: continue

	#uncomment the below to print on terminal
	#print track_title, artist_name, track_length, album_title, genre_name, track_rating, track_count

	#insert data into tables
	#because the "name" is UNIQUE, we use "INSERT OR IGNORE"
	cur.execute('''INSERT OR IGNORE INTO Artist (name)
		VALUES ( ? )''', (artist_name, ));
	#select the first row and save the id in artist_id
	cur.execute('SELECT id from Artist WHERE name = ( ? )''', (artist_name, ))
	#save the id in artist_id
	artist_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Genre (name)
		VALUES ( ? )''', (genre_name, ));
	#select the first row
	cur.execute('SELECT id from Genre WHERE name = ( ? )''', (genre_name, ))
	#save the id in genre_id
	genre_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
		VALUES ( ?, ? )''', ( album_title, artist_id ));
	#select the first row
	cur.execute('SELECT id from Album WHERE title = ( ? )''', (album_title, ))
	#save the id in album_id
	album_id = cur.fetchone()[0]

	#if the record exists, REPLACE it. Function is similar to IGNORE used above
	cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
		VALUES ( ?, ?, ?, ?, ?, ?)''', ( track_title, album_id, genre_id, track_length, track_rating, track_count ))

	#commit the changes
	conn.commit()