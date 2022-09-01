import readline


def main():
    i=0
    infile=open('clients.txt','r')

    for x in infile:
        i+=1
        #x=x.rstrip('\n')
        print(str(i) + '.' + ' '+ x.rstrip('\n'))
        #print(i,'. ',line,sep='') Professor B way
main()