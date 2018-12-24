import numpy as np
from tempfile import TemporaryFile
data = TemporaryFile()

def nonlin(x, d = False):
	if (d == True):
		return (x*(1-x))
	
	return 1/(1+np.exp(-x))
	
print('Content-Type: text/plain')
print('')

x = np.array((np.loadtxt("data_cb.txt",delimiter=":",usecols = (0,1,2,3,4),dtype = 'int')-3)/2)

print (x)
print("\n")

y = np.array([np.loadtxt("data_cb.txt",delimiter=":",usecols = 5,dtype = 'int')/500]).T

ds = y.size

np.random.seed(1)

syn0 = 2*np.random.random((5,ds)) - 1
syn1 = 2*np.random.random((ds,ds-1)) - 1
syn2 = 2*np.random.random((ds-1,1)) - 1


for j in range(100000):
	
	l0 = x
	l1 = nonlin(np.dot(l0,syn0))
	l2 = nonlin(np.dot(l1,syn1))
	l3 = nonlin(np.dot(l2,syn2))

	l3_error = y - l3
	if (j % 10000) == 0:
                print ("error:" + str(np.mean(np.abs(l3_error))))
                print("\n")
				
	l3_delta = l3_error*nonlin(l3,d = True)
	l2_error = l3_delta.dot(syn2.T)
	l2_delta = l2_error*nonlin(l2,d = True)
	l1_error = l2_delta.dot(syn1.T)
	l1_delta = l1_error*nonlin(l1,d = True)

	syn2 += l2.T.dot(l3_delta)
	syn1 += l1.T.dot(l2_delta) 
	syn0 += l0.T.dot(l1_delta)

print("\n")
print(syn0)
print("\n")
print(syn1)
print("\n")
print(syn2)

np.savez('data_cb', syn0=syn0,syn1=syn1,syn2=syn2)

data.close()


print('\n\ndone')




