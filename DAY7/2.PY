from tkinter import *

first_number =second_number =operator=None

def get_digit(digit):
    current = result_label('text')
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')   

def get_operator(op):
    global first_number,operator
    first_number = int(result_label['text'])
    operator=op
    result_label.config(text='')   

def get_result():
    global first_number, second_number,operator
    second_number= int[result_label['text']]
    if operator =='+':
    result_label.config(text=str(first_number+second_number))
    elif operator =='-':
    result_label.config(text=str(first_number - second_number))
    elif operator =='*':
    result_label.config(text=str(first_number x second_number))
    elif operator =='/':
    result_label.config(text=str(first_number / second_number))
        