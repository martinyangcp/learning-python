from tkinter import *


def add():
    filee =open("Phone_book.dat","a")
    filee.write(blank1.get() + blank2.get() + "\n")
    blank1.delete(0,END)
    blank2.delete(0,END)
    filee.close()

def first():
    pass

def next():
    pass

def prebut():
    pass

def lastbut():
    pass

def readfile():
    filee =open("Phone_book.dat","r")
    filee.read()
    filee.close()
    

window = Tk()

name = Label(window,text="이름")
blank1= Entry(window)
name.grid(row=0 ,column =0, columnspan = 2)
blank1.grid(row=0 ,column =2,columnspan = 4)

phonenumber = Label(window,text="전화번호")
blank2= Entry(window)
phonenumber.grid(row=1 ,column =0, columnspan=2)
blank2.grid(row=1 ,column =2,columnspan = 4)

addbut = Button(window,text = "추가", command=add)
firstbut = Button(window,text = "처음")
nextbut = Button(window,text = "다음")
prebut = Button(window, text = "이전")
lastbut = Button(window,text = "마지막")
readfile = Button(window,text = "파일 읽기")

addbut.grid(row=2 ,column =0)
firstbut.grid(row=2 ,column =1)
nextbut.grid(row=2 ,column =2)
prebut.grid(row=2 , column=3)
lastbut.grid(row=2 ,column =4)
readfile.grid(row=2 ,column =5)

window.mainloop()