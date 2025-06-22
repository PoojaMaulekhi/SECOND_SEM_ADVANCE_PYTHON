
import numpy as np
import pandas as pd
# pandas=> data analysis and series.

# string 
country=['India','pakistan','USA', 'NEPAL']
print(pd.Series(country))
# complete table=> data
# Series=> tabel ki single row or single series.


# inetgeres
runs=[13,36,78,90]
print(pd.Series(runs))
# 0    13  note=> ishma yeh "index" automatic hi aati hai.
# 1    36
# 2    78
# 3    90


# print no of both arrays
# here we have customize the index.
# by default 0,1,2,3 hi rahega   
marks=[67,57,89,90]
subjects=['maths','english','science','hindi']
print(pd.Series(marks,index=subjects))

# setting a name
print(pd.Series(marks,index=subjects,name='pooja'))
# marks







