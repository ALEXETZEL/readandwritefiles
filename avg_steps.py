import csv
from signal import default_int_handler

infile= open('steps.csv','r')
outfile=open('avg_steps.csv','w')

csvfile=csv.reader(infile, delimiter=',')

i=0
a=0

next(csvfile)

prof_b=['January','February','March', 'April', 'May', 'June', 'July' 
,'August', 'Septemer', 'October', 'November','December']
month=1

outfile.write('Month, Average Steps\n')
for x in csvfile:
    print(x)
    print(i)
    if float(x[0])!=month:
        month-=1
        avg=(a/i)
        avg=format(avg,',.2f')
        print(prof_b[month]+', '+str(avg))
        outfile.write(prof_b[month]+', '+ str(avg)+'\n')
        month+=2
        i=0
        a=0
    if float(x[0])==month:
        a+=float(x[1])
        i+=1
month-=1
avg=(a/i)
avg=format(avg,',.2f')
print(prof_b[month]+', '+str(avg))
outfile.write(prof_b[month]+', '+ str(avg)+'\n')
outfile.close()