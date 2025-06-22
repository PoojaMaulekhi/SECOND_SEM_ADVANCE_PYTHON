# Create class

class Student:
    name="Pooja"

s1=Student() # object create (object also called Instance)
s1.name # access name attribute of class 



#constructor
class Student:

    def __init__(self):  # non parameterized constructor
       print("non parameterized")

    def __init__(self,name):  # parameterized constructor
        self.name=name #name=>argunment value ,,
        #self =>point towards that object. 
        #self.name=>ush object ka andar value dal rahe hai. 
        print("parameterized")

s1=Student()
print(s1)

s2=Student("pooja")
print(s2.name) # yeh name value 




# Class and object Attribute 
# class=>jo sabhi object mai common hai
# object=>