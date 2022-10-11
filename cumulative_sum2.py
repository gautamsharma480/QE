import numpy as np
import sys

filename = 'total-dos.dat' #sys.argv[1]
ev2ry = 1/13.605698066
ry2ev = 1/ev2ry
bohr2angs = 0.529177249 

f = open('nscf.out', 'r')
f_pw = f.readlines()
f.close()

for line in f_pw:
    if 'highest occupied, lowest unoccupied level' in line:
       #if shift_gap == 0:
          VBM = float(line.split()[6])
          CBM = float(line.split()[7])
          Fermi = (VBM+CBM)*0.5
          print('Fermi=', Fermi,'eV',  Fermi*ev2ry,'Ry')   

get_TDOS = np.loadtxt(filename) 
#print(Fermi,'Final Fermi')
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
		
f.close()
#cum_sum = np.cumsum(get_TDOS_Ef) 
print ("cumulative sum of array elements: ",b)

mu_vs_cc = np.loadtxt('a.dat')
cc = []

def closest(lst, K): 
     lst = np.asarray(lst) 
     idx = (np.abs(lst - K)).argmin() 
     return idx 

#with open('values.dat', 'w') as f: 
for i in range(0,len(mu_vs_cc)):
#        f.write('x')
        cc.append(mu_vs_cc[i,1])

#print(cc)
#print(int(mu_vs_cc[-1][1]-2))
index1 = closest(cc, int(mu_vs_cc[-1][1]))          
print(index1)
index2 = closest(cc, int(mu_vs_cc[-1][1]-2))
print(index2)
print(mu_vs_cc[index1,0]-mu_vs_cc[index2,0], (mu_vs_cc[index1,1]-mu_vs_cc[index2,1]))

