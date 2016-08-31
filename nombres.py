#aptitude install python-numpy
import numpy as np
def registro(archivo): 
    name=[]
    last_name =[]
    with open(archivo, "r+") as f:
	data = f.readlines()
 	name = [x.split() for x in data]
	last_name = np.array(name)[:,1]
    	name = np.array(name)[:,0]
	name.sort()
    	last_name.sort()
	print name, last_name
	j=0
	i=0
	while i<len(name):
	    f.seek(j)
	    write=name[i]+' '+last_name[i]+ '\n'
    	    f.write(write)
	    j=j+len(write)
	    i=i+1

    #for line in infile.readlines():
    #	print line
#	names= line.split(' ')
#	print names
#	name.append(names[0]) 
#        last_name.append(names[1])
#    name.sort()
#    last_name.sort()
#    i=0
#    print name, last_name
#    infile.close()
#    write = open('registro.txt', 'w')
#    while i<len(name): 
#	write.write(name[i]+' '+last_name[i])
#        i=i+1
	
#    write.close()

if __name__ == "__main__":
    registro('registro.txt')
