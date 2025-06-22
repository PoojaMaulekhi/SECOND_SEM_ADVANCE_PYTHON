#MEMORY
import numpy as np
a=[i for i in range(1000)]

import sys
print(sys.getsizeof(a)/1024)

a=np.arange(1000,dtype=np.int32)
print(sys.getsizeof(a)/1024)

# numpy =>less memory occupy karta hai.
#tha