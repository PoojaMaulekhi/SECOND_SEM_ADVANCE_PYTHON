# DATAFRAME

import numpy as np
import pandas as pd


subs=pd.read_csv('./datasets-session-16/subs.csv')
movies=pd.read_csv('./datasets-session-16/movies.csv')
ipl=pd.read_csv('./datasets-session-16/kohli_ipl.csv')

print(movies.info())

# using lists
student_data=[
    [100,80,10],
    [120,100,14],
    [80,50,2]
]

print(pd.DataFrame(student_data,columns=['iq','marks','package']))


# using dictionary

student_data={
    'name':['nitish','ankit','rupesh'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,60,50,40],
    'package':[10,2,7,2,0,0]
}
# print(pd.DataFrame(student_data,columns=['name','iq','marks','package']))

