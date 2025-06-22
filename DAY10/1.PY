import matplotlib.pyplot as plt

x=[1,2,3]
y=[2,4,1]

plt.plot(x,y)
plt.show()

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# multiple graph 
x=[3,7,8]
y=[9,10,12]
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multiple Graph")
plt.plot(x,y,color="green")


x1=[9,78,90]
y1=[2,4,7]
plt.plot(x1,y1,color="red")
plt.show()

# legend =>display legends
# loc=> loc decide the place where legend will display.