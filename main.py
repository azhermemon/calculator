from tkinter import *
import os

def btnClick(number):
    global operator
    operator=operator+str(number)
    input_text.set(operator)

def btnClear(opr):
    global operator
    operator=''
    input_text.set(operator)

def btnEquals(oper):
    global operator
    sump = str(eval(operator))
    input_text.set(sump)
    operator=''


root = Tk()

root.title("CALCULATOR")
root.geometry('450x520')
operator = ''
root.configure(background="orange")
root.resizable(0,0)
input_text = StringVar()

black1= Label(root, bg="black", width='47', height='13')
black1.place(x=10, y= 11)

calculator = Label(root, text='CALCULATOR', bg='orange', fg='white',width='15', height='1', font=('times', 25, 'bold'))
calculator.place(x=125, y=10)

text = Entry(root, textvariable=input_text, bg='orange', fg='black', width='28', font=('times', 25, 'bold'), justify='right')
text.place(x=30, y=80)

black2 = Label(root, bg='black', width='47', height='18')
black2.place(x=10, y=220)

#number panel lable

numlab = Label(root, bg='white', height='17', width='30')
numlab.place(x=30, y=140)

#operation panel

oppanel = Label(root, bg='orange', height='17', width='8')
oppanel.place(x=315, y=140)

#line first /

button7 = Button(root, text='7', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(7), activebackground='orange')
button7.place(x=38, y=160)


button8 = Button(root, text='8', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(8), activebackground='orange')
button8.place(x=135, y=160)

button9 = Button(root, text='9', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(6), activebackground='orange')
button9.place(x=225, y=160)

buttonDV = Button(root, text='/', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick('/'), activebackground='orange')
buttonDV.place(x=325, y=160)


#line second *

button6 = Button(root, text='6', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(6), activebackground='orange')
button6.place(x=38, y=210)

button5 = Button(root, text='5', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(5), activebackground='orange')
button5.place(x=135, y=210)

button4 = Button(root, text='4', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(4), activebackground='orange')
button4.place(x=225, y=210)

buttonMP = Button(root, text='*', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick('*'), activebackground='orange')
buttonMP.place(x=325, y=210)


#line third +

button3 = Button(root, text='3', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(3), activebackground='orange')
button3.place(x=38, y=260)

button2 = Button(root, text='2', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(2), activebackground='orange')
button2.place(x=135, y=260)

button1 = Button(root, text='1', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(1), activebackground='orange')
button1.place(x=225, y=260)

buttonPlus = Button(root, text='+', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick('+'), activebackground='orange')
buttonPlus.place(x=325, y=260)

#forth line '=', "-" & "Clear" Operation

buttonc = Button(root, text='C', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClear('c'), activebackground='orange')
buttonc.place(x=38, y=330)

button0 = Button(root, text='0', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick(0), activebackground='orange')
button0.place(x=135, y=330)

buttonEqu = Button(root, text='=', bg='black', fg='orange', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnEquals('='), activebackground='orange')
buttonEqu.place(x=225, y=330)

buttonMinus = Button(root, text='-', bg='black', fg='black', width='4', height='1', font=('times', 25, 'bold'), command=lambda:btnClick('-'), activebackground='orange')
buttonMinus.place(x=325, y=330)



root.mainloop()

