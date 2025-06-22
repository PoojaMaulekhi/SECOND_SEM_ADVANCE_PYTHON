# enclosing 

def outer():
    y = 20  # Enclosing scope
    def inner():
        print(y)  # Accesses 'y' from outer function
    inner()  # Output: 20

outer()


# its called closure .
def outer():          #1,3               
    x=5               #4
    def inner:        #5(inner ka andar nhi jayega ,kyuki function call nhi hui hai)  10(inner excute)     
        print x       # (it returns x)  
    return inner      # 6(outer na "inner" only return kiya)             
b= outer()            #2,7 (b has inner) 9(inner() function execute hua)
b()                   #8
