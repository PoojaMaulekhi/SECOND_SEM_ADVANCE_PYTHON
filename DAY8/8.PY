# The ravel() function in NumPy is used to flatten a multi-dimensional array
#  into a 1D array.

import numpy as np

a3 = np.array([
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
    [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
    [[18, 19, 20], [21, 22, 23], [24, 15, 16]]
])

#  nditer is  for iteration in  3D 
for i in np.nditer(a3):
    print(i)

print(a3.ravel())
