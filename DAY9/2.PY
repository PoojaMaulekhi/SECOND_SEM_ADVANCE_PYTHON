
import numpy as np
import pandas as pd

# dictionary mai index check nhi karenga.
# by default=> key=index.
marks={
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series=pd.Series(marks,name='pooja')
print(marks_series.size) #4 
print(marks_series)
print(marks_series.dtype) # for data type.
print(marks_series.is_unique) #koi element agar same hua toh false show karega.
print(marks_series.index)
