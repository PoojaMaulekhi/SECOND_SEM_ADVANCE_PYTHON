
import numpy as np
import pandas as pd

subs=pd.read_csv('./datasets-session-16/subs.csv')
movies=pd.read_csv('./datasets-session-16/movies.csv')
movies=pd.read_csv('./datasets-session-16/kohli_ipl.csv')

# print(subs)
# print(subs.head()) #top 5


# print(movies)
# print(movies.head()) #top 5
print(movies.count()) #top 5
# print(subs.sort_values(ascending=True,by='runs').head(1).values[0])
print("###########   Line break   ##########")
print(subs.sum())


print(movies[1::2]) # fancy slicing 
