import math
import numpy as np 
import sys

## i have not used this definition in this code 
def  prn(x0,x1,x2,n):   ## printing nn number of digits after decimal 
        if n == 3:
            xx0 = '%.3f' % x0
            xx1 = '%.3f' % x1
            xx2 = '%.3f' % x2
        else:
            xx0 = '%.5f' % x0
            xx1 = '%.3f' % x1
            xx2 = '%.3f' % x2
        return xx0 , xx1 , xx2

# bohr is bigger unit , not using bohr to get percentages  
print('lattice parameter in angstrom')
lattice_parameter = 2.951795352 #angstrom 
#lattice_parameter = float(sys.argv[1])
a = [0.0, 0.01,0.02,0.03,0.04,0.05]
b = []
c = []
d = [ '%.8f' %  0.0, '%.8f' %  0.0, 14.999999085]
print('For Plus strain  ')

for i in a:
    one_percentage = i * lattice_parameter  
    new_lattice_parameter = lattice_parameter + one_percentage 
    #print(new_lattice_parameter)
    b = [new_lattice_parameter , '%.8f' %  0.0 , '%.8f' % 0.0] 
    c = [-new_lattice_parameter*0.5, new_lattice_parameter*math.sqrt(3)*0.5, '%.8f' % 0.0] 
    print('!' ,i)
    print('CELL PARAMETERS  angstrom')
    print(b[0],b[1],b[2])
    print(c[0],c[1],c[2]) 
    print(d[0],d[1],d[2])
    print('            ')
print('           ')
print('           ')
#print('           ')

print('For Minus strain  ')

for i in a:
    one_percentage = i * lattice_parameter
    new_lattice_parameter = lattice_parameter - one_percentage
    #print(new_lattice_parameter)
    b = [new_lattice_parameter , '%.8f' %  0.00000 , '%.8f' % 0.00000]
    c = [-new_lattice_parameter*0.5, new_lattice_parameter*math.sqrt(3)*0.5, '%.8f' % 0.00000]
    print('!' , -1*i)
    print('CELL PARAMETERS  angstrom')
    print(b[0],b[1],b[2])
    print(c[0],c[1],c[2])
    print(d[0],d[1],d[2])
    print('            ')

