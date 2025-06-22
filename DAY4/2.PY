class PHONE:
    def __init__(self,price,brand,camera):
        print("main phone class constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

class SmartPhone(PHONE):
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
        print("inside  smartphone constructor")

s=SmartPhone("Android",2)
s.os