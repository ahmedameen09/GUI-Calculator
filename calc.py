from tkinter import *
import math

# functions

X = 0
flag = 0

def click1():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "1")
    X = X + 1

def click2():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "2")
    X = X + 1

def click3():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "3")
    X = X + 1

def click4():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "4")
    X = X + 1

def click5():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "5")
    X = X + 1

def click6():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "6")
    X = X + 1

def click7():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "7")
    X = X + 1

def click8():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "8")
    X = X + 1

def click9():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "9")
    X = X + 1

def click0():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, "0")
    X = X + 1

def clickP():
    global X
    global var1
    global flag
    var1 = box1.get()
    box1.delete(0, END)
    box1.insert(X, "+")
    flag = 1
    X = X + 1

def clickN():
    global X
    global var1
    global flag
    var1 = box1.get()
    box1.delete(0, END)
    box1.insert(X, "-")
    flag = 2
    X = X + 1

def clickE():
    global X
    global var1
    var1 = float(var1)
    var2 = box1.get()
    var2 = float(var2)
    box1.delete(0,END)
    if flag == 1 :
        result = var1 + var2
    elif flag == 2 :
        result = var1 - var2
    elif flag == 3 :
        result = var1 * var2
    elif flag == 4 :
        result = var1 / var2
    else :
        pass

    d , whole = math.modf(result) #for taking the after decimal and know if it int or not
    if d == 0 :
        box1.insert(0, int(result))
    else :
        formatf = "{:.2f}".format(result)
        box1.insert(0, formatf)

def clickC():
    box1.delete(0 , END)
    global X
    X = 0

def clickD():
    global X
    if box1.get() == "+" or box1.get() == "-" or box1.get() == "×" or box1.get() == "÷" :
        box1.delete(0, END)
    box1.insert(X, ".")
    X = X + 1

def clickM():
    global X
    global var1
    global flag
    var1 = box1.get()
    box1.delete(0, END)
    box1.insert(X, "×")
    flag = 3
    X = X + 1

def clickd():
    global X
    global var1
    global flag
    var1 = box1.get()
    box1.delete(0, END)
    box1.insert(X, "÷")
    flag = 4
    X = X + 1

# Creating Screens

mainw = Tk()
mainw.title("Ameen Calculator")

# creating the window widget

box1 = Entry (mainw, bg = "white" , fg = "black" , width = 43 , borderwidth=5 )
btn1 = Button(mainw, text = "1", padx=40, pady=20, command=click1)
btn2 = Button(mainw, text = "2", padx=40, pady=20, command=click2)
btn3 = Button(mainw, text = "3", padx=40, pady=20, command=click3)
btn4 = Button(mainw, text = "4", padx=40, pady=20, command=click4)
btn5 = Button(mainw, text = "5", padx=40, pady=20, command=click5)
btn6 = Button(mainw, text = "6", padx=40, pady=20, command=click6)
btn7 = Button(mainw, text = "7", padx=40, pady=20, command=click7)
btn8 = Button(mainw, text = "8", padx=40, pady=20, command=click8)
btn9 = Button(mainw, text = "9", padx=40, pady=20, command=click9)
btn0 = Button(mainw, text = "0", padx=40, pady=20, command=click0)
btnP = Button(mainw, text = "+", padx=48, pady=20, command=clickP)
btnN = Button(mainw, text = "-", padx=49, pady=20, command=clickN)
btnM = Button(mainw, text = "×", padx=48, pady=20, command=clickM)
btnE = Button(mainw, text = "=", padx=39.5, pady=20, command=clickE)
btnD = Button(mainw, text = ".", padx=42, pady=20, command=clickD)
btnC = Button(mainw, text = "CLS", padx=42, pady=20, command=clickC)
btnd = Button(mainw, text = "÷", padx=48, pady=20, command=clickd)

# Putting objects on screen

box1.grid(row = 1 , column = 0 , columnspan=3 , padx=10 , pady=15)
btn1.grid(row = 4 , column = 0)
btn2.grid(row = 4 , column = 1)
btn3.grid(row = 4 , column = 2)
btn4.grid(row = 3 , column = 0)
btn5.grid(row = 3 , column = 1)
btn6.grid(row = 3 , column = 2)
btn7.grid(row = 2 , column = 0)
btn8.grid(row = 2 , column = 1)
btn9.grid(row = 2 , column = 2)
btn0.grid(row = 5 , column = 0)
btnP.grid(row = 2 , column = 3)
btnM.grid(row = 3 , column = 3)
btnN.grid(row = 4 , column = 3)
btnE.grid(row = 5 , column = 2)
btnC.grid(row = 1 , column = 3)
btnD.grid(row = 5 , column = 1)
btnd.grid(row = 5 , column = 3)

mainw.mainloop()