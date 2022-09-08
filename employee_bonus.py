import csv

infile=open("EmployeePay.csv",'r')

csvfile=csv.reader(infile, delimiter=',')


next(csvfile)

for record in csvfile:
    sal=float(record[3])
    bon=float(record[4])
    bonus=(bon*sal+sal)
    print('ID: ' +record[0])
    print('Employee First Name: ' +record[1])
    print('Employee Last Name: '+record[2])
    print('Total Pay: ' + '$' + format(bonus,',.2f'))
    input()


