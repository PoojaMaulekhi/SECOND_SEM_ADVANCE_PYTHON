import numpy as np

array = np.array([
        [[0,1,2],[3,4,5],[6,7,8]],
        [[9,10,11],[12,13,14],[15,16,17]],
        [[18,19,20],[21,22,23],[24,25,26]]
        ])

# Extract 12, 13 from matrix 1, row 1, columns 0-1
# slice1 = arr[1, 1, 0:2]   # [12,13]

# Extract 21, 22 from matrix 2, row 1, columns 0-1
# slice2 = arr[2, 1, 0:2]   # [21,22]


# for i in np.diter(a3):
#     print(i)