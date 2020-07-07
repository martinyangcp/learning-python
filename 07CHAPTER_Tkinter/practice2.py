from tkinter import *

def calc():
    cm = int(entry1.get())*2.54
    label4["text"] = str(cm)+"센티미터"

window = Tk()
                                                   
label1 = Label(window,text="인치를 센티미터로 변환하는 프로그램")
label1.grid(row=0, column=0, columnspan=2)

label2 = Label(window,text="인치를 입력하시오 :")
label2.grid(row=1,column=0)
entry1 = Entry(window)
entry1.grid(row=1,column=1)

label3 = Label(window,text="반환결과 :")
label3.grid(row=2,column=0)
label4 = Label(window, text="결과값이 출력됩니다.")
label4.grid(row=2, column=1)

button1 = Button(window,text="변환", command = calc)
button1.grid(row=3,column=1)

window.mainloop()