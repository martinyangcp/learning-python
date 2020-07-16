
from tkinter import *

window =Tk()



def f11(): 
    summ.insert(END, str(7))
def f12(): 
    summ.insert(END, str(8))
def f13(): 
    summ.insert(END, str(9))
def f14(): 
    summ.insert(END, "/")
def f15(): 
    summ.delete(0,END)
def f21(): 
    summ.insert(END, "4")
def f22(): 
    summ.insert(END, "5")
def f23(): 
    summ.insert(END, "6")
def f24(): 
    summ.insert(END, "*")
def f31(): 
    summ.insert(END, "1")
def f32(): 
    summ.insert(END, "2")
def f33(): 
    summ.insert(END, "3")
def f34(): 
    summ.insert(END, "-")
def f41(): 
    summ.insert(END, "0")
def f42(): 
    summ.insert(END, ".")
def f43(): 
    ans = eval(summ.get())
    summ.delete(0,END)
    summ.insert(END,str(ans))
def f44(): 
    summ.insert(END, "+")


summ = Entry(window, bg="yellow")
summ.grid(row=0, column=0 ,columnspan = 5)

but11=Button(window, text = "7", command =f11)
but12=Button(window, text = "8", command =f12)
but13=Button(window, text = "9", command =f13)
but14=Button(window, text = "/", command =f14)
but15=Button(window, text = "C", command =f15)

but11.grid(row=1, column=0)
but12.grid(row=1, column=1)
but13.grid(row=1, column=2)
but14.grid(row=1, column=3)
but15.grid(row=1, column=4)


but21=Button(window, text = "4", command =f21)
but22=Button(window, text = "5", command =f22)
but23=Button(window, text = "6", command =f23)
but24=Button(window, text = "*", command =f24)
but25=Button(window, text = "")

but21.grid(row=2, column=0)
but22.grid(row=2, column=1)
but23.grid(row=2, column=2)
but24.grid(row=2, column=3)
but25.grid(row=2, column=4)

but31=Button(window, text = "1", command =f31)
but32=Button(window, text = "2", command =f32)
but33=Button(window, text = "3", command =f33)
but34=Button(window, text = "-", command =f34)
but35=Button(window, text = "")

but31.grid(row=3, column=0)
but32.grid(row=3, column=1)
but33.grid(row=3, column=2)
but34.grid(row=3, column=3)
but35.grid(row=3, column=4)

but41=Button(window, text = "0", command =f41)
but42=Button(window, text = ".", command =f42)
but43=Button(window, text = "=", command =f43)
but44=Button(window, text = "+", command =f44)
but45=Button(window, text = "")

but41.grid(row=4, column=0)
but42.grid(row=4, column=1)
but43.grid(row=4, column=2)
but44.grid(row=4, column=3)
but45.grid(row=4, column=4)

window.mainloop()
