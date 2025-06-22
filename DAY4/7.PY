class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone")
        self.__price=price
        self.brand=brand
        self.camera=camera

class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        print("Inside Smartphone")
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("Inside Smartphone")

s=SmartPhone(200,"Samsung",12,"Android","ram",4)
print(s.os)
print(s.brand)