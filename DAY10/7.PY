import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('./datasets-session-16/Book.csv')

print(data.columns)  # List all column names

plt.plot(data['AGE'],data['SALES'])          #bar  
plt.xlabel('Age')
plt.ylabel('Sales')
plt.grid() 
plt.show()