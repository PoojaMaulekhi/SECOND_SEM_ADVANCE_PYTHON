
import numpy as np
import pandas as pd

marks={
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series=pd.Series(marks,name='Marks of all subjects')
print(marks_series)
marks_series[0]=9000
print(marks_series)
