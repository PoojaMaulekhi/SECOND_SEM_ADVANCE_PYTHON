# decorator =>flow 

def sanitary_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                raise TypeError("no")
        return inner_wrapper
    return outer_wrapper

@sanitary_check(int)
def square(num):
    print (num**2)
@sanitary_check(str)
def greet(name):
    print("Hello",name)

