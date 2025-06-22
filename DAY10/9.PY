# stacked plot
import matplotlib.pyplot as plt

months=['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
sales_car=[120,30,56,89,120,34,78,2,45 ,62,76,51]
sales_bike=[240,27,34,56,78,89,90,67,32,62,76,51]

plt.stackplot(months,sales_car,sales_bike,labels=['car','bike'])
plt.legend()
plt.title("car vs bike sale")
plt.show()