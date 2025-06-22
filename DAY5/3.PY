class A:
    def m1(self):
        return 20
    
class B(A):
    def m1(self):
        return 30

    def m2(self):
        return 40   
    
class C(B):
    def m2(self):
        return 20   

obj1=A()
obj2=B()
obj3=C() 
print(obj1.m1()+obj3.m1()+obj3.m2())
#obj1.m1() =20
#obj3.m1() =30
#obj3.m2() =20 child class override parent class.