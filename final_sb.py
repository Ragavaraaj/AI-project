import numpy as np
from tempfile import TemporaryFile
data = TemporaryFile()

def nonlin(x, d = False):
        if (d == True):
                return (x*(1-x))
        
        return 1/(1+np.exp(-x))
        
print('Content-Type: text/plain')
print('')

x = np.array((np.loadtxt("data_sb.txt",delimiter=":",usecols = (0,1,2,3,4,5),dtype = 'int')-3)/2)

print (x)
print("\n")


y = np.array([np.loadtxt("data_sb.txt",delimiter=":",usecols = 6,dtype = 'int')/1200]).T

ds = y.size

np.random.seed(1)

syn0 = 2*np.random.random((6,ds)) - 1
syn1 = 2*np.random.random((ds,1)) - 1


for j in range(100000):
        
        l0 = x
        l1 = nonlin(np.dot(l0,syn0))
        l2 = nonlin(np.dot(l1,syn1))

        l2_error = y - l2
        if (j % 10000) == 0:
                print("error:" + str(np.mean(np.abs(l2_error))))
                print("\n")
                
        l2_delta = l2_error*nonlin(l2,d = True)
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = l1_error*nonlin(l1,d = True)
        
        syn1 += l1.T.dot(l2_delta) 
        syn0 += l0.T.dot(l1_delta)  

print(syn0)
print("\n")
print(syn1)
print("\n")

np.savez('data_sb', syn0=syn0,syn1=syn1)

data.close()

print('\n\ndone')
