class Parent:
    def __init__(self):
        self.num=100 #value initialize kar di hai.

class Child(Parent):
    def __init__(self):
        super().__init__() #main function ko call kari hai
        self.var=200

    def show(self):
        print(self.num)
        print(self.var)

son=Child()
son.show()
