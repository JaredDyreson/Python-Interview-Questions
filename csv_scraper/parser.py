#!/usr/bin/env python3.5

import csv
# basically can take in a CSV file and print all of its contents along with the ammount of elmements are in the file
# adapted from this code here ->  https://realpython.com/python-csv/

with open('data.csv') as f:
	csv_reader = csv.reader(f, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if(line_count == 0):
			print("Column names are: {}".format(", ".join(row)))
		else:
			print("{}".format(", ".join(row)))
		line_count += 1
	print("Processed {} amount of lines".format(line_count))
	
