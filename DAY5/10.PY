# NON-LOCAL KEYWORD

def outer():
    a=1 #Enclosing Scope.
    def inner():
        nonlocal a
        a+=1
        print("inner", a)

    inner()
    print('Outer', a)

outer()
print("Main program")
