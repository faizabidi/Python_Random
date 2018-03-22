# Run it with python3

import numpy as np
import cmath
from elasticsearch import helpers, Elasticsearch
import csv
import subprocess
import time

# Open the file
file = open("data.dat", "r")

# Extract binary data. dtype is uint8 because each part is an unsigned number between 0-255.
dt = np.dtype(int)
array = np.fromfile(file, dtype='uint8')
print("Number of bytes in the file is %s" %len(array))

# 1, 3, 5... and so on are all part1s in the "array" of type numpy.ndarray 
# Similarly, 2, 4, 6....and so on are all part2s in the  "array"
# Let's create a list for each part
part1_real_list = array[0::2]
part2_imag_list = array[1::2]

print("Number of real numbers in the list is %s" %len(part1_real_list))
print("Number of imaginary numbers in the list is %s" %len(part2_imag_list))

# Average the numbers in the two lists
average_real = sum(part1_real_list) / len(part1_real_list)
average_imag = sum(part2_imag_list) / len(part2_imag_list)

print("Average of real numbers is %s" %average_real)
print("Average of imaginary numbers is %s" %average_imag)

# Making complex numbers and storing in a list
list_complex_numbers = list()
for real, imag in zip(part1_real_list, part2_imag_list):
    z = str(complex(real, imag))
    list_complex_numbers.append(z)

# Storing in Elastic search
# Let's first output our data to a csv file as well
with open("csv_complex_numbers.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in list_complex_numbers:
        writer.writerow([val])
print("csv file containing all the complex numbers is created by the name csv_complex_numbers.csv")

print("Now adding indexes to Elasticsearch...")
# Index in the ES assuming localhost is running the server
es = Elasticsearch()

# Delete if old index "faiz-index" exists
if es.indices.exists("faiz-index"):
    res = es.indices.delete(index = "faiz-index")

# Index data
with open("csv_complex_numbers.csv") as file:
    reader = csv.DictReader(file)
    helpers.bulk(es, reader, index='faiz-index', doc_type='faiz-type')

time.sleep(3)
print("Checking indices on ES...")
subprocess.call("curl -XGET 'localhost:9200/_cat/indices?v'", shell=True)
