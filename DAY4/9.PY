# MULTILEVEL

class Product:
    def review(self):
        print("Product customer review")

class Phone(Product):
    def __init__(self,price,brand,camera):
        print("Phone customer review")       
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")

class SmartPhone (Phone):
    pass

s=SmartPhone(900, "Apple",12)
s.buy()
s.review()

