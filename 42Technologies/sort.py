import csv

inp = raw_input ('Enter file name: ')

#if user just presses enter, read the default file
try:
	if len (inp) < 1 : inp = 'data.tsv'
	input_file = open (inp)
	#skip the top row
	next (input_file)
except:
	print 'File not found!'
	exit ()

d = dict ()
lst = list()

#store data in a dictionary
for rows in input_file:
	rows = rows.rstrip ().split ('|')
	d[float (rows[3])] = rows[0:]

#convert sorted dictionary to list
for key, value in sorted(d.iteritems()):
    value = [value]
    lst.append(value)

headers = ['property0','property1','property2','net_sales','net_sales_units']

#write the data to a file
with open ("new_data.tsv", "wb") as myfile:
	wr = csv.writer(myfile, delimiter = '|')
	wr.writerow (headers)
	wr.writerows(lst)