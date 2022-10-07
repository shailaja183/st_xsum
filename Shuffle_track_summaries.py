import re

def merge(summlist, shuffleorder):
	c = 1
	cs = ""
	for i in shuffleorder:
		cs+="Summary "+str(c)+": "+summlist[i-1]+"\n"
		c+=1 
	return(cs.strip('\n'))

def split(strdump, shuffleorder):
	ordersumm = []
	splitsumm = []
	for i in strdump.split('\n'):
		splitsumm.append(re.sub(r'^Summary \d: ','',i))
	for i in range(0,len(shuffleorder)):
		ordersumm.append(splitsumm[shuffleorder.index(i+1)])
	return ordersumm
