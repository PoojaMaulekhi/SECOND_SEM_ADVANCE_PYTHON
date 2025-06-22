# power function
def power(a=5,b=6):
    print(a**b)
    return a**b
power()


# def multiply(*args):
#     product=1

#     for i in args:
#      product=product*i

#     print(args)
#     return product

def project(name,language=':::python'):
   print(name,language)
   return

project("Online exam system", "java") #correct
project(language ='C++', name="java")  #correct
project("data analysis")  #correct
project(language="java")  # error , jiski default value(name)  set nhi kari hai , usha pas nhi kiya hai..

