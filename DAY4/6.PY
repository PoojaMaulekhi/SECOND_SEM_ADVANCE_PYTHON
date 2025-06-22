# SUPER KEYWORD

class Phone:
    def __init__(self,price,brand):
        print("inside phone")
        self.price=price
        self.brand=brand
        
    def buy(self):
       print("phone class")


class SmartPhone(Phone):
    def buy(self):
        print("SmartPhone class") 

        super().buy() #super keyword

s=SmartPhone(2000,'Apple')
s.buy()   
# super => can access it outside the class 
# isha uski bas parent class hi acces hi kar sakti hai. 