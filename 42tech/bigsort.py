import csv
from collections import defaultdict

inp = raw_input ('Enter file name: ')

#if user just presses enter, read the default file
try:
	if len (inp) < 1 : inp = 'unsortedData.tsv'
	input_file = open (inp)
	#skip the top row
	next (input_file)
except:
	print 'File not found!'
	exit ()

#create a dictionary that can store duplicate keys as well
d = defaultdict (list)

#property0 acts as the key
for rows in input_file:
	rows = rows.rstrip ().split ('|')
	
	property0 = rows[0]
	property1 = rows[1]
	property2 = rows[2]
	net_sales = rows[3]
	net_sales_units = rows[4]

	details = (property0, property1, property2, net_sales, net_sales_units)

	d[property0].append (details)

#print all keys for property0, which are 6 in number
#print d.keys ()

#check number of unique keys using "print len (d)". 
#It's 5 in this case. So, create 5 lists
accessories = list ()
kids_footwear = list ()
mens_footwear = list ()
product_care = list ()
womens_footwear = list ()

#bigList will contain all the smallers lists
bigList = list ()

#create a list for each unique key found in property0
for key, value in d.items ():
	if (key == '$total'):
		#add this to the top of the bigList
		bigList.extend (value)

	elif (key == 'accessories'):
		accessories.append (value)

	elif (key == 'kids footwear'):
		kids_footwear.append (value)

	elif (key == 'mens footwear'):
		mens_footwear.append (value)

	elif (key == 'product care'):
		product_care.append (value)
	
	elif (key == 'womens footwear'):
		womens_footwear.append (value)

#######################################################################################
#print accessories
#create a big list for accessories
bigList_Accessories = list ()

men_list = list ()
big_men_list = list ()

eye_list = list ()
big_eye_list = list ()

handbags_list = list ()
big_handbags_list = list ()

belts_list = list ()
big_belts_list = list ()

small_leather_list = list ()
big_small_leather_list = list ()

giftable_list = list ()
big_giftable_list = list ()

for i in accessories:
	for j in i:
		#print j
		if j[1] == '$total' and j[2] == '$total':
			bigList_Accessories.append (j[0:])
		
		elif j[1] == 'men':
			if j[2] == '$total':
				big_men_list.append (j[1:])
			else:
				men_list.append (j[1:])
		
		elif j[1] == 'eye':
			if j[2] == '$total':
				big_eye_list.append (j[1:])
			else:
				eye_list.append (j[1:])

		elif j[1] == 'handbags':
			if j[2] == '$total':
				big_handbags_list.append (j[1:])
			else:
				handbags_list.append (j[1:])

		elif j[1] == 'belts':
			if j[2] == '$total':
				big_belts_list.append (j[1:])
			else:
				belts_list.append (j[1:])

		elif j[1] == 'small leather goods':
			if j[2] == '$total':
				big_small_leather_list.append (j[1:])
			else:
				small_leather_list.append (j[1:])

		else:
			if j[2] == '$total':
				big_giftable_list.append (j[1:])
			else:
				giftable_list.append (j[1:])

#check which total is biggest using the big lists
#sort the list by sales
handbags_list = sorted (handbags_list, key=lambda sales: float(sales [2]), reverse=True)
#add "accessories" keyword
men_list = [(''.join("accessories"),) + l for l in men_list]
big_men_list = [(''.join("accessories"),) + l for l in big_men_list]
#add to the big list
big_men_list.extend (men_list)
#print big_men_list

#sort the list by sales
eye_list = sorted (eye_list, key=lambda sales: float(sales [2]), reverse=True)
#add "accessories" keyword
eye_list = [(''.join("accessories"),) + l for l in eye_list]
big_eye_list = [(''.join("accessories"),) + l for l in big_eye_list]
#add to the big list
big_eye_list.extend (eye_list)
#print big_eye_list

#sort the list by sales
handbags_list = sorted (handbags_list, key=lambda sales: float(sales [2]), reverse=True)
#add "accessories" keyword
handbags_list = [(''.join("accessories"),) + l for l in handbags_list]
big_handbags_list = [(''.join("accessories"),) + l for l in big_handbags_list]
#add to the big list
big_handbags_list.extend (handbags_list)
#print big_handbags_list


#sort the list by sales
belts_list = sorted (belts_list, key=lambda sales: float(sales [2]), reverse=True)
#add "accessories" keyword
belts_list = [(''.join("accessories"),) + l for l in belts_list]
big_belts_list = [(''.join("accessories"),) + l for l in big_belts_list]
#add to the big list
big_belts_list.extend (belts_list)
#print big_belts_list

#sort the list by sales
small_leather_list = sorted (small_leather_list, key=lambda sales: float(sales [2]), reverse=True)
#add "accessories" keyword
small_leather_list = [(''.join("accessories"),) + l for l in small_leather_list]
big_small_leather_list = [(''.join("accessories"),) + l for l in big_small_leather_list]
#add to the big list
big_small_leather_list.extend (small_leather_list)
#print big_small_leather_list

#sort the list by sales
giftable_list = sorted (giftable_list, key=lambda sales: float(sales [2]), reverse=True)
#add "accessories" keyword
giftable_list = [(''.join("accessories"),) + l for l in giftable_list]
big_giftable_list = [(''.join("accessories"),) + l for l in big_giftable_list]
#add to the big list
big_giftable_list.extend (giftable_list)
#print big_giftable_list

#add all the smaller lists to the big accessory list.
#add order was checked using the $total value obtained in big_xxxx_list
bigList_Accessories.extend (big_handbags_list)
bigList_Accessories.extend (big_men_list)
bigList_Accessories.extend (big_small_leather_list)
bigList_Accessories.extend (big_eye_list)
bigList_Accessories.extend (big_belts_list)
bigList_Accessories.extend (big_giftable_list)
#print bigList_Accessories[0]

#######################################################################################
#print kids_footwear
#create a big list for kids_footwear
bigList_kids_footwear = list ()

kids_list = list ()
big_kids_list = list ()

baby_list = list ()
big_baby_list = list ()

for i in kids_footwear:
	for j in i:
		#print j
		if j[1] == '$total' and j[2] == '$total':
			bigList_kids_footwear.append (j[0:])
		
		elif j[1] == 'kids':
			if j[2] == '$total':
				big_kids_list.append (j[1:])
			else:
				kids_list.append (j[1:])

		elif j[1] == 'baby':
			if j[2] == '$total':
				big_baby_list.append (j[1:])
			else:
				baby_list.append (j[1:])

#print kids_list

#sort the list by sales
kids_list = sorted (kids_list, key=lambda sales: float(sales [2]), reverse=True)
#add "kids footwear" keyword
kids_list = [(''.join("kids footwear"),) + l for l in kids_list]
big_kids_list = [(''.join("kids footwear"),) + l for l in big_kids_list]
#add to the big list
big_kids_list.extend (kids_list)
#print big_kids_list

#sort the list by sales
baby_list = sorted (baby_list, key=lambda sales: float(sales [2]), reverse=True)
#add "kids footwear" keyword
baby_list = [(''.join("kids footwear"),) + l for l in baby_list]
big_baby_list = [(''.join("kids footwear"),) + l for l in big_baby_list]
#add to the big list
big_baby_list.extend (baby_list)
#print big_baby_list

#add all the smaller lists to the big kids_footwear list
#add order was checked using the $total value obtained in big_xxxx_list
bigList_kids_footwear.extend (big_kids_list)
bigList_kids_footwear.extend (big_baby_list)
#print bigList_kids_footwear[0]

#######################################################################################
#print mens_footwear
#create a big list for mens_footwear
bigList_mens_footwear = list ()

boots_list = list ()
big_boots_list = list ()

shoes_list = list ()
big_shoes_list = list ()

for i in mens_footwear:
	for j in i:
		#print j
		if j[1] == '$total' and j[2] == '$total':
			bigList_mens_footwear.append (j[0:])
		
		elif j[1] == 'boots':
			if j[2] == '$total':
				big_boots_list.append (j[1:])
			else:
				boots_list.append (j[1:])

		elif j[1] == 'shoes':
			if j[2] == '$total':
				big_shoes_list.append (j[1:])
			else:
				shoes_list.append (j[1:])

#sort the list by sales
boots_list = sorted (boots_list, key=lambda sales: float(sales [2]), reverse=True)
#add "mens footwear" keyword
boots_list = [(''.join("mens footwear"),) + l for l in boots_list]
big_boots_list = [(''.join("mens footwear"),) + l for l in big_boots_list]
#add to the big list
big_boots_list.extend (boots_list)
#print big_boots_list

#sort the list by sales
shoes_list = sorted (shoes_list, key=lambda sales: float(sales [2]), reverse=True)
#add "mens footwear" keyword
shoes_list = [(''.join("mens footwear"),) + l for l in shoes_list]
big_shoes_list = [(''.join("mens footwear"),) + l for l in big_shoes_list]
#add to the big list
big_shoes_list.extend (shoes_list)
#print big_shoes_list

#add all the smaller lists to the big mens footwear list
#add order was checked using the $total value obtained in big_xxxx_list
bigList_mens_footwear.extend (big_boots_list)
bigList_mens_footwear.extend (big_shoes_list)
#print bigList_mens_footwear[0]

#######################################################################################
#print product_care
#create a big list for product_care
bigList_product_care = list ()

product_care_list = list ()
big_product_care_list = list ()

for i in product_care:
	for j in i:
		#print j
		if j[1] == '$total' and j[2] == '$total':
			bigList_product_care.append (j[0:])
		elif j[1] == 'product care':
			if j[2] == '$total':
				big_product_care_list.append (j[1:])
			else:
				product_care_list.append (j[1:])

#sort the list by sales
product_care_list = sorted (product_care_list, key=lambda sales: float(sales [2]), reverse=True)
#add "product care" keyword
product_care_list = [(''.join("product care"),) + l for l in product_care_list]
big_product_care_list = [(''.join("product care"),) + l for l in big_product_care_list]
#add to the big list
big_product_care_list.extend (product_care_list)
#print big_product_care_list

#add all the smaller lists to the big mens footwear list
#add order was checked using the $total value obtained in big_xxxx_list
bigList_product_care.extend (big_product_care_list)
#print bigList_product_care[0]

#######################################################################################
#create a big list for mens_footwear
bigList_womens_footwear = list ()

wboots_list = list ()
big_wboots_list = list ()

wshoes_list = list ()
big_wshoes_list = list ()

for i in womens_footwear:
	for j in i:
		#print j
		if j[1] == '$total' and j[2] == '$total':
			bigList_womens_footwear.append (j[0:])
		
		elif j[1] == 'boots':
			if j[2] == '$total':
				big_wboots_list.append (j[1:])
			else:
				wboots_list.append (j[1:])

		elif j[1] == 'shoes':
			if j[2] == '$total':
				big_wshoes_list.append (j[1:])
			else:
				wshoes_list.append (j[1:])

#sort the list by sales
wboots_list = sorted (wboots_list, key=lambda sales: float(sales [2]), reverse=True)
#add "womens footwear" keyword
wboots_list = [(''.join("womens footwear"),) + l for l in wboots_list]
big_wboots_list = [(''.join("womens footwear"),) + l for l in big_wboots_list]
#add to the big list
big_wboots_list.extend (wboots_list)

#sort the list by sales
wshoes_list = sorted (wshoes_list, key=lambda sales: float(sales [2]), reverse=True)
#add "womens footwear" keyword
wshoes_list = [(''.join("womens footwear"),) + l for l in wshoes_list]
big_wshoes_list = [(''.join("womens footwear"),) + l for l in big_wshoes_list]
#add to the big list
big_wshoes_list.extend (wshoes_list)

#add all the smaller lists to the big womens footwear list
#add order was checked using the $total value obtained in big_xxxx_list
bigList_womens_footwear.extend (big_wshoes_list)
bigList_womens_footwear.extend (big_wboots_list)

#######################################################################################

#add all sublist to one big list, and print the file out
bigList.extend (bigList_womens_footwear)
bigList.extend (bigList_mens_footwear)
bigList.extend (bigList_Accessories)
bigList.extend (bigList_kids_footwear)
bigList.extend (bigList_product_care)

headers = ['property0', 'property1', 'property2', 'net_sales', 'net_sales_units']

#write the data to a file
with open ("sortedData.tsv", "wb") as myfile:
	wr = csv.writer(myfile, delimiter = '|')
	wr.writerow (headers)
	wr.writerows(bigList)