# operator overloading

class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x-other.x
    
p1=A(5)
p2=A(3)
print(p1+p2)
#Normally, + performs addition, but operator overloading allows us to redefine its behavior.
# Here, + is overloaded to perform subtraction instead.