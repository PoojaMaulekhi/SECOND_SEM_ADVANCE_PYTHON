import numpy as np

# Define a 3D array (2x2x2)
array = np.array([
    [[0, 1], [2, 3]],  # First 2D "block"
    [[4, 5], [6, 7]]   # Second 2D "block"
])

array = np.array([
    [0, 1, 2, 3],  
    [4, 5, 6, 7],
    [9,11,8,10]  
])

print(array[0:1,]) #first row
print(array[0:1,]) #second row

# print(array[0, 1, 0]) 