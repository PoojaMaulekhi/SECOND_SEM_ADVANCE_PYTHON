# A Python Function defined inside a
# class is called a method

class DOG:
    attr1 = "Mammal"
    attr2 = "DOG"

    def fun(self):
     print("I am a",self.attr1)
     print("I am a",self.attr2)
     print(id(self))

Rodger=DOG()
print(Rodger.attr1)
print(Rodger.attr2)

# self is a object, reference variable which point towards the function itself 


class Room:
   l=5.0
   b=4.0

   def calculateArea(self):
      area=(self.l * self.b)
      print(area)

study_room=Room()
study_room.calculateArea()

