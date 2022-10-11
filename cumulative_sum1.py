import numpy as np
import sys

filename = sys.argv[1] # Enter density of states or any data file for which you want to find cumulative sum.
Fermi = float(sys.argv[2])

get_TDOS = np.loadtxt(filename) 

print(get_TDOS.shape)

#print(get_TDOS[0,:])
#print(get_TDOS[0][:])
get_TDOS_Ef = np.zeros(len(get_TDOS), dtype=float)
#print(Fermi)
ai = 0
af = 0
b = 0
#print(get_TDOS_Ef)
f = open('a.dat', 'w')
for i in range(0,len(get_TDOS)):
	af = get_TDOS[i,0] - Fermi #i+1
	#print(a)
	if af <= 0:
		#print(i,af,get_TDOS[i,1])
		if i==0: ai = af
		b = b + get_TDOS[i,1]*(af - ai) # f0 + f(i+1)*(E(i+1) - E(i))
		get_TDOS_Ef[i] = b
		f.write(str(af) + '     '+ str(b) + '\n')
	ai = af	#i	
		
#cum_sum = np.cumsum(get_TDOS_Ef) 
print ("cumulative sum of array elements: ",b)

