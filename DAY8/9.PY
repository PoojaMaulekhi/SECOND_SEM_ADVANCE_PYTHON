
# stacking 
import numpy as np
a1=np.arange(25).reshape(6,4)
a1.hsplit(a1,6)
a1.vsplit(a1,4)


x=np.arange(11,23).reshape(3,4)
print(x)
y=x.ravel()
z=x.flatten()  # create a copy of original array.
print(y)
print(z)
y[1]=100
