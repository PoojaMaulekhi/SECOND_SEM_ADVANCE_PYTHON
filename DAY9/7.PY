
import numpy as np
import pandas as pd

movies=pd.read_csv('./datasets-session-16/movies.csv')l

print(movies.info())  
print("******************")

print(movies.isnull())
print("******************")

print(movies.isnull().sum())
print("******************")

print(movies.duplicated())
print("******************")

print(movies.duplicated().sum())
print("******************")

print(movies['title_x'])

print(movies[['year_of_release','actors','title_x']])

print(movies.iloc[[0,4,5]])
