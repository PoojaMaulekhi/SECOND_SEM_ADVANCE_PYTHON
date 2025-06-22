
from tkinter import *
root = Tk()

# Configure window
root.geometry("750x550")  # Use "x"(Alphabet vala) instead of "*" for dimensions
root.title("COunter  Button")
counter=0

def click():
    global counter
    global mylabel
    counter =counter+1
# configure=> attach a value with label.
    mylabel.configure(text=f'you clicked me{counter}')
    if counter>10:
        mybutton.configure(state=DISABLED)
        mylabel.configure(text="sorry")
mylabel=Label(root,text="no click",fg="white",bg="black",pady=0)
mylabel.pack()
mybutton=Button(root,text="Click me",command=click,padx=30)
mybutton.pack(pady=50)
root.mainloop()