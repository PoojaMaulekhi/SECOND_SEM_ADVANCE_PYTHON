import matplotlib.pyplot as plt

# Manually define data
age = [25, 30, 35, 40, 45, 50, 55, 60]
income = [40000, 55000, 60000, 80000, 75000, 90000, 95000, 110000]

# Create scatter plot
plt.scatter(age, income, color='blue', edgecolor='black', alpha=0.7)
plt.title('Age vs Income')
plt.xlabel('Age (years)')
plt.ylabel('Income ($)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()