# Aggregation 

class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def print_address(self):
        print(self.address.city, self.address.pin,self.address.state)


class Address:
    def __init__(self,city,pin,state):
        self.city=city #initialize 
        self.pin=pin
        self.state=state

    def get_city(self):
        return self.city
    

add1 = Address('gurgaon' ,122011 , 'haryana')
cust=Customer('nitish','male',add1)

cust.print_address()