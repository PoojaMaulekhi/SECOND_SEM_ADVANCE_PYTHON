def my_decorator(func):             #1      
    def wrapper():                  #
        print("*****")              #    
    func()                          #
        print("*****")              #    
    return wrapper                  #
def hello():                        #
    print("hello")                  #
def display():                      #
    print("hello nitish")           #
a=my_decorator(hello)               #    
a()                                 #
a=my_decorator(display)             #    
    


def deco_add(fun): #1(execute nhi hoga kyuki , function call nhi kari hai), 4(fun=add)
    def square(a,b): #5(function call nhi hui) ,9 (square(5,7))
        c=fun(a,b)   # 10(add(5,7)) ,13(c=12)
        return c*c   # 14( 12*12 = 144)
    return square    #6(square return )

def add(x,y): #2(nhi run hoga) ,11
    return x+y  #8 , 12(return 5+7 =12)

add=deco_add(add) #3 , 7(add=square , ka barabar )
print(add(5,7))#8(here call to,, square(5,7))




import time
def  timer(func):
    def wrapper(args):
        start = time.time()
        func(*args)
        print("Time taken by ", func.__name__.time.time().start,'secs')
        return wrapper 

