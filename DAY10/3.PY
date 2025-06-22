import matplotlib.pyplot as plt


# INTERSECTING GRAPHS

X=[1,8,13,6,5]
Y=[2,4,21,3,5]

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Graph with corner points")
plt.plot(X,Y,color='red',marker='o',markersize=10,markerfacecolor='green')
plt.show()


