#DECORATOR

def func():
    print("Hello")

f= func
f()


#python are 1st class  function.
def modify(func,name): # main function 
    return func(num)

def square(num): # decorator function 
    return num**2

modify(square,2)