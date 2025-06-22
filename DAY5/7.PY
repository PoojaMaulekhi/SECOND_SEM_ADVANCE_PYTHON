#LOCAL AND GLOBAL

#1
a=2 #global
def temp():
    b=3 #local for temp function.
    print(b)

temp()
print(a) 

#function jaise hi value return karenga ,vaisa hi uska scope khatam..


#2 same variable name hona seh kuch farak nhi pdta. 
a=2 #global
def temp():
    a=3 #local for temp function.
    print(a)

temp()
print(a) 

#variable agar local mai defined nhi hai toh ,
#  usha global mai find karnga apna ap hi 
# O/p =>2, 2
a=2 
def temp():
    print(a)

temp()
print(a)


# access global variable locally..
# O/P=> 3
a=2 
def temp():
    global a 
    a+=1   # yha par 'a' ki global value update hogi., isliye yeh last mai o/p 3 dega..
    print(a)

temp()
print(a)



# function parameter is local
def temp(z):
    print(z)

a=5
temp(5)
print(a)
print(z) #can access local (z) globally..


