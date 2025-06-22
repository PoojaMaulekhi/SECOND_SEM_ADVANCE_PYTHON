
from tkinter import *
root = Tk()

# Configure window
root.geometry("750x550")  # Use "x"(Alphabet vala) instead of "*" for dimensions
root.title("Entry Widget textbox")
txt=Text(root)
txt.configure(bg='SteelBlue2',height=2)
txt.insert('1.0',"enter the data")
name=' '
def submit():
    global name
    name=txt.get("1.0","1.3")
    mylabel=Label(root,text=name,width=120)
    mylabel.pack()
txt.delete('1.0','1.3')
button=Button(root,text='submit',command=submit)
button.pack()
