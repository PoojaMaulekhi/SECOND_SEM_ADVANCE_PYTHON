# METHOD OVERRIDING

# child and parent class mai agar same function hai toh 
# function call hona par,, child class parent class ko override kar degi.

class Phone:
    def __init__(self,price,brand):
        print("inside phone")
        self.price=price
        self.brand=brand
        
    def buy(self):
       print("phone class")


class SmartPhone():
    def buy():
        print("SmartPhone class") 

s=SmartPhone()
s.buy()
