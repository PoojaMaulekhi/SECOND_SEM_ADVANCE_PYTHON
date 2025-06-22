
# __add__  method =>

num=10
x=num+5
print(x)

# add using magic method
num=10
x=num.__add__(10)
print(x)


# string 
num='4'
x=num+'5'
print(x)

# string add using magic method
num='hlw'
x=num.__add__('pooja')
print(x)



#  __gt__ => 

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=self.m1+other.m2

        if r1>r2:
            return True
        else:
            return False
        
# __str__  =>custom string.
def  __str__(self):
    return F"The name is hlw {self.name}"

#  __new__  => add new instance in class