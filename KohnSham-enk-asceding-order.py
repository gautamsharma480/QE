import numpy as np 
import sys 
prefix = sys.argv[1]
minE = float(sys.argv[2])
maxE = float(sys.argv[3])

f = open('nscf.out', 'r')
f_pw = f.readlines()
f.close()
shift_gap = 0 
for line in f_pw:
    if 'highest occupied, lowest unoccupied level' in line:
       if shift_gap == 0:
          VBM = float(line.split()[6])
          CBM = float(line.split()[7])
          Fermi = (VBM+CBM)*0.5
          #print('Fermi=', Fermi,'eV' ) 
    if 'Fermi' in line:
          Fermi = float(line.split()[4])
print('Fermi=', Fermi,'eV' )
enk = np.loadtxt(prefix+'.energy')

#print(enk)
#print(enk.shape)
cc=[]
#for j in range(0,enk.shape[1]):
for i in range(0,enk.shape[0]):
#        f.write('x')
           cc.append(enk[i])


#print(len(cc))
#print(cc.size)
def count(list1, l, r):
    c = 0 
    # traverse in the list1
    for x in list1:
        # condition check
        y=[]
        if x>= l and x<= r:
            print(x ,x-Fermi)
            c+= 1 
            #y.append(x) 
    #print(y.sort())      
    #print(y)  
    return  c  

x=np.where(np.logical_and(enk>=minE, enk<=maxE))[0]
#x.flatten()
#print(x)
xs = [enk[i] for i in x]
xs.sort()
print(xs)
'''for i in x:
     print(enk[i])'''
print(count(cc,minE,maxE))
