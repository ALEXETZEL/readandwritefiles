import csv
from signal import default_int_handler

infile= open('steps.csv','r')
outfile=open('avg_steps.csv','w')

csvfile=csv.reader(infile, delimiter=',')

yo=0
i=0
balls=0

next(csvfile)

prof_b=['January','February','March', 'April', 'May', 'June', 'July' 
,'August', 'Septemer', 'October', 'November','December']
month=1

outfile.write('Month, Average Steps\n')
for x in csvfile:
    balls+=float(x[1])
    i+=1
    if float(x[0])!=month:
        month-=1
        avg=(balls/i)
        avg=format(avg,',.2f')
        print(prof_b[month]+', '+str(avg))
        outfile.write(prof_b[month]+', '+ str(avg)+'\n')
        month+=2
    if float(x[0])==month:
        balls+=float(x[1])
        i+=1
    
outfile.close()