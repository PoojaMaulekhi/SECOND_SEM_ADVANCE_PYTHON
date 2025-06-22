# POLYMORPHISM
#METHOD OVERLOADING

#1 thats how METHOD OVERLOADING achieve .
class Shape:
    def area(self, a, b=0):
        if b==0:
            return 3.14*a*b
        else:
            return a*a
        
s=Shape()
print(s.area(2))
print(s.area(2,3))

#2 METHOD OVERLOADING => it show error.
# class Shape:
#     def area(self,a,b):
#         return a*b
#     def area(self,a):
#         return 3.14*a*a
    
# s=Shape()
# print(s.area(2))
# print(s.area(2,3))