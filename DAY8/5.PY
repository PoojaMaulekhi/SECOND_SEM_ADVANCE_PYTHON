import numpy as np

a1=np.arange(10,dtype=np.int32)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print(a3)

# 32=>4 bit
# 64=>8 bit


#  datatype 
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

a1=np.arange(12).reshape(3,4) # GENRATE MATRIX
print(a1)

# SACLAR OP
# matrix mai sara arithmetic operation lag sakta hai 
# ARITHMETIC
print(a1+a2)
print(a1-a2)
print(a1 **2)
print(a1<a2)
print(a1>a2)

np.max(a1,axis=1)
np.var(a1,axis=1)
np.var(78890)


a1=np.arange(12).reshape(3,4)
a2=np.arange(12).reshape(4,3)
# dot product
print(np.dot(a1,a2))

# indexing and slicing

a1=np.arange(10)
a2=np.arange(10).reshape(3,4)
a3=np.arange(10).reshape(4,3)
print(a1[9])

# indexing in matrix (python) starts from 0.(not 1)