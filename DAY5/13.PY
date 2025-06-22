def mydisplay(fun):
    def inner(name_ref):
        print("Hello",end=" ")
        fun(name_ref)
        print("Good BYe")
        return inner