# ITERATION

#jispa loop chala sakta hai =>iterable 
# iterator=> store single value.
# both used in deep learning => 

# each iterable is iterator.
# each iterator is  not iterable.

L =[x for x in range(1,10)]
for i in L:     # here L is iterable.
    print(i*2)  # i is iterator 
# so this is iterable object.


import sys
print(sys.getsizeof(L)/64)

x=range(1,10)

for i in x:         
    print(i*2)


print(sys.getsizeof(x)/64)

#iterable => puri list store hogi   e.g (L) 
#iterator => onli single value.     e.g (x)