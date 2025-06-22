import numpy as np

# V=U+A*T GRAPH
u=20
a=5
v=[]
t=np.arange(2,21)
for i in t:
    v.append(u+a*i)
print(t)
print(v)