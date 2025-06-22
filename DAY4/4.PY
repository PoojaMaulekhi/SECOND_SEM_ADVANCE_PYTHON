# we cant access parent class's private variable by the help of child class.

class Parent:
    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num
    
class Child(Parent): #thats how  inherit the clases in python. Child inherit parent class
    def show(self):
        print("This is in Child Class")

    def display(self):
        print(self._Child__num)

son=Child(100)
print(son.get_num())
son.show()
son.display()
