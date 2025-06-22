# PLOT THE GRAPH
import matplotlib.pyplot as plt

# plt.plot(t,v)
plt.xlim(5,15)
plt.ylim(50,25)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("v vs x graph")
plt.grid(True)
plt.legend()
plt.show()