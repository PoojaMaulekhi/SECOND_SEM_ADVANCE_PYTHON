
from tkinter import *
root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable('0,0')
root.configure(background='black')

result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,)
result_label.config(font='')




btn1=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=2,column=1)
btn1.config(font=('verdana',14))


btn2=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=2,column=1)
btn2.config(font=('verdana',14))


btn3=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=2,column=1)
btn3.config(font=('verdana',14))


btn4=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=1)
btn4.config(font=('verdana',14))


btn5=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))


btn6=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=1)
btn6.config(font=('verdana',14))


btn7=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=2,column=1)
btn7.config(font=('verdana',14))


btn8=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=2,column=1)
btn8.config(font=('verdana',14))


btn9=Button(root,text='5',bg="#00a65a",fg='white',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=2,column=1)
btn9.config(font=('verdana',14))


btn_sub =Button(root,text='-', bg='#00a65a', fg='white',width=5,height=2,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))       