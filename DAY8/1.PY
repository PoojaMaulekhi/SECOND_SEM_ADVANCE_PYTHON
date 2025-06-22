# pythonlist=>	Heterogeneous , Less efficient	
# numpy array=>	Homogeneous ,	More efficient


#NUMPY 
import numpy as np
a=np.arange(1000)
b=np.arange(1000,2000)



#Speed

#List
a=[i for i in range(1000)]
b=[i for i in range(1000,2000)]

c=[]
import time
# time.time() => gives time to run that code
start=time.time() # before start the programm.
for i in range(len(a)):
    c.append(a[i]+b[i])
print(time.time()-start) #after end of  programm
# time.time()-start => net time to execute a code.