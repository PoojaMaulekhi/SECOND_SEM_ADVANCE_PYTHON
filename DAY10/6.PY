import matplotlib.pyplot as plt

age=[2,4,5,6,7,20,40,76,45,89,90,45,67]
range=(0,100)
inter=10

# hist => to plot histogram
plt.hist(age,inter,range,color='green')
plt.xlabel('Age')
plt.ylabel('No of Persons')

plt.title('Age distribution plot')
plt.show()