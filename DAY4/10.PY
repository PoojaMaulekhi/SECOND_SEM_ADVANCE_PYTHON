# HIERARCHICAL

class Phone:
    def __init__(self,price,brand,camera):
        print("phone inside constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("buy a phone")

class SmartPhone(Phone):
    def __init__(self,price,brand,camera):
        print("phone inside Smartphone")
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(100,"Apple","13px").buy()
FeaturePhone(10,"Lava","1px").buy()

# child class ka constructor ko call karenga toh sabsa pehla 