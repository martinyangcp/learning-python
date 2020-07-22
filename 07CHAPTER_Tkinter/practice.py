from tkinter import *

window = Tk()

num = 0

def add():
    global num
    num += int(entry.get())
    n_num["text"] = str(num)

def subtract():
    global num
    num -= int(entry.get())
    n_num["text"] = str(num)

def clear():
    global num
    num = 0
    n_num["text"] = str(0)
    entry.delete(0, END)

hab = Label(window,text="현재 합계")
hab.grid(row=0, column=0)
n_num = Label(window,text= num)
n_num.grid(row=0, column=1, columnspan=2)

entry = Entry(window)
entry.grid(row=1, column=0,columnspan=3 )

addbut= Button(window, text="더하기(+)", command = add)
addbut.grid(row=2, column=0)
subbut= Button(window, text="빼기(-)", command = subtract)
subbut.grid(row=2, column=1)
clrbut= Button(window, text="초기화", command = clear)
clrbut.grid(row=2,column=2)

window.mainloop()