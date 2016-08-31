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
	j=0
	i=0
	while i<len(name):
	    f.seek(j)
	    write=name[i]+' '+last_name[i]+ '\n'
    	    f.write(write)
	    j=j+len(write)
	    i=i+1
if __name__ == "__main__":
    registro('registro.txt')
