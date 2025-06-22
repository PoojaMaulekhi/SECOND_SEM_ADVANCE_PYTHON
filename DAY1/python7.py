# def var_key(**vark):
#     print("all keyword argunments are",vark)
#     return

# var_key(a=10,b=20,c=30) #correct
# var_key() #empty dictionary
# var_key(a=10) # {'a': 10}


def var_key1(**vark1):
    for v in vark1:
        print(v, vark1[v])
    return

var_key1(a=10,b=20,c=30)
