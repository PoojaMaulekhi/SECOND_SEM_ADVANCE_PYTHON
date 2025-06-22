# ABSTRACTION
# TO HIDE 
# abstrct mtehod always in parent class 
# child class inherit parent class
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class (cannot be instantiated)
    @abstractmethod
    def make_sound(self):  # Must be implemented in child classes
        pass

class Dog(Animal):
    def make_sound(self):  # Overrides abstract method
        return "Bark!"

class Cat(Animal):
    def make_sound(self):  # Overrides abstract method
        return "Meow!"

# animal = Animal()  ❌ Error: Can't instantiate abstract class
dog = Dog()
print(dog.make_sound())  # ✅ Output: "Bark!"

cat = Cat()
print(cat.make_sound())  # ✅ Output: "Meow!"