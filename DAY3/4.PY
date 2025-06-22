# INHERITANCE

class User:
    def __init__(self):
        self.name='nitish' 
        self.gender='male'

        def login(self):
            print('login')


class Student(User):
    def __init__(self):
        self.rollno=100

    def enroll(self):
        print("enroll into course")


u=User()
s=Student()