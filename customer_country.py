import csv
from signal import default_int_handler

infile= open('customers.csv','r')
outfile=open('customer_country.csv','w')

csvfile=csv.reader(infile, delimiter=',')

next(csvfile)

outfile.write("full name, country\n")

for record in csvfile:
    name=record[1]+' '+record[2]
    country=record[4]
    outfile.write(name + ' '+country+ '\n')

outfile.close()

