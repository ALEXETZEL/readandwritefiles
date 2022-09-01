import csv
infile= open('customers.csv','r')

csvfile=csv.reader(infile, delimiter=',')

next(csvfile) #this will skip the first row

for record in csvfile:
    print('ID:',record[0])
    print('Fname:',record[1])
    print('Lname:',record[2])
    print('City:',record[3])
    print('State:',record[4])
    print('Phone Number:', record[5])
    input()

#lists arr 0 based index


