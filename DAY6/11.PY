
from tkinter import *
root = Tk()

# Configure window
root.geometry("750x550")  # Use "x"(Alphabet vala) instead of "*" for dimensions
root.title("Entry Widget textbox")

ent=Entry(root,borderwidth=5,width=30)
ent.pack()
def click():
    x=ent.get()
    mylabel=Label()
    mylabel.pack()
    ent.delete(0,END)

mybutton=Button(root,text="Enter",command=click)
mybutton.pack()
root.mainloop()