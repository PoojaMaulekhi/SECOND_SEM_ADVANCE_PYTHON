#single level inheritance.

class Phone:
    def __init__(self,price,brand,camera):
        print("phone inside constructor")
        self.price=price
        self.brand=brand
        self.camera=camera


    def buy(self):
        print("buy a phone")

class smartPhone(Phone):
    pass

s=smartPhone(2000,"apple",13)
s.buy()