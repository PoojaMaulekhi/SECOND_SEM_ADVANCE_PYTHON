import matplotlib.pyplot as plt

#  FOR MULTIPLE GRAPH

x=[1,23,4]
y=[4,6,8]

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("Multiple Graph")
plt.plot(x,y,color='red',linestyle='--',label='line-1')

x1=[9,78,90]
y1=[2,4,7]
plt.plot(x1,y1,color="green",linestyle='--',label='line-2')
plt.legend() # call before show function..
plt.show()
