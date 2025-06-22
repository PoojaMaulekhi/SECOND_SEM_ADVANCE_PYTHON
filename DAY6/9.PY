from tkinter import *

root = Tk()

# Configure window
root.geometry("750x550")  # Use "x"(Alphabet vala) instead of "*" for dimensions
root.title("Adding Label")

# Create label widgets
mylabel1 = Label(root, text="Hello students", background="pink")
mylabel2 = Label(root, text="NIET students", background="green")

# Place labels in window using grid
mylabel1.grid(row=0, column=0)  # Fixed variable name (mylabel1 instead of mylabel)
mylabel2.grid(row=0, column=1)  # Fixed variable name (mylabel2 instead of mylabel)

root.mainloop()