def var_len1(pos,*var):
    print("one position argunment",pos)
    print("remaining parameters are in tuple", var)
    print("aceessing tuple elemnts one by one")

    for v in var:
        print(v)
    return

var_len1()