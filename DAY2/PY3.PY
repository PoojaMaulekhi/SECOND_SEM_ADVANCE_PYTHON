# CONSTRUCTOR

class Person:
    def __init__(self,name): #init method
        self.name=name

    def say_hi(self):
            print("Hello my name is", self.name)

p=Person('Sofia')

p.say_hi()
# flow=>  class(Person)>say_hi(function)> init(itself call hui constructor ko)







class DOG:
    animal='dog'
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

Rodger=DOG("Pug","brown")
Buzo=DOG("Bulldog","black")
print("\n Rodger details")
print('Rodger details', Rodger.animal)
print('Rodger details', Rodger.breed)
print('Rodger details', Rodger.color)
print("\n Buzo details")
print('Rodger details', Buzo.animal)
print('Rodger details', Buzo.breed)
print('Rodger details', Buzo.color)







class Person:
     def __init__(self):
          self.name='Maneesh'
          self.gender='Male'

p=Person()
print(p.name)

q=p
print(id(p))  # for id of a give value
print(id(q))
q.name="Rahul"
print(p.name)
# print(p.name)

