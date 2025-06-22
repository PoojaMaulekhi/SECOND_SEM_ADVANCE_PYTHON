class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone")
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("buy a phone")


class Product:
    def buy(self):
        print("buy a phone in phone")  

class SmartPhone(Phone,Product):# jo class pehla passs hogi , vhi pehla path jayega .
    pass

s=SmartPhone(200,"Apple",12)

s.buy()
#  SmartPhone is SmartPhone → Phone → Product → object. 
# So it finds __init__ in the Phone class first