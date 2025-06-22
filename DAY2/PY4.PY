# class(point) > x,y (coordinate)


#code to print cordinates 
class POINT:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
     return '<{},{}>'.format(self.x,self.y)
    
x=int(input("Enter first no x"))
y=int(input("Enter first no y"))

obj=POINT(x,y)
print(obj)

#  formula to find distance
