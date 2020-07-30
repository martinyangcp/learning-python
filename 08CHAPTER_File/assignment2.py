from tkinter import *

def add():
    infile = open("Phone_book.dat.txt","w")
    infile.write(nameentry.get(),phoneentry.get())
    infile.close()

def first():
    infile = open("Phone_book.dat.txt","r")
    infile.readlines()
    infile.close()

def next():
    infile = open("Phone_book.dat.txt","r")
    infile.readlines()
    infile.close()

def pre():
    infile = open("Phone_book.dat.txt","r")
    infile.readlines()
    infile.close()

def last():
    infile = open("Phone_book.dat.txt","r")
    infile.readlines()
    infile.close()
    
def readfile():
    infile = open("Phone_book.dat.txt","r")
    infile.readlines()
    infile.close()



window =Tk()

name = Label(window, text = "이름")
name.grid(row = 0, column =0)
nameentry = Entry(window)
nameentry.grid(row = 0 ,column = 2,columnspan=3)


phone = Label(window, text ="전화번호")
phone.grid(row = 1 , column = 0)
phoneentry = Entry(window)
phoneentry.grid(row = 1 , column = 2,columnspan=3)

addbut = Button(window, text ="추가", command = )
addbut.grid(row = 2 , column = 0)
firstbut = Button(window, text ="처음", command =)
firstbut.grid(row = 2 , column = 1)
nextbut = Button(window, text ="다음", command = )
nextbut.grid(row = 2 , column = 2)
prebut = Button(window, text ="이전" , command =)
prebut.grid(row = 2 , column = 3)
lastbut = Button(window, text ="마지막" , command =)
lastbut.grid(row = 2 , column = 4)
readfile = Button(window, text ="파일 읽기", command =)
readfile.grid(row = 2 , column = 5)
window.mainloop()