# #button creation
from tkinter import *
root=Tk()

#static button , here state normal rakhni hai..
static_btn = Button(root, text="Static Button", state="normal")
static_btn.pack()
root.mainloop()


#clickable button


# Use "x"(Alphabet vala) instead of "*" for dimensions
root.geometry("750x550") 
root.title("event trigger")

def click():
    mylabel=Label(root,text="u click",fg="white",bg="black",pady=20,font=25)
    mylabel.pack()
mylabel=Button(root,text="Click me", command=click,padx=30)
mylabel.pack(pady=50)
root.mainloop()

