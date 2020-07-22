from tkinter import *

window = Tk()
label1=Label(window,text="화씨")
label2=Label(window,text="섭씨")
entry1=Entry(window)
entry2=Entry(window)
button1 = Button(window,text="화씨->섭씨")
button2 = Button(window,text="섭씨->화씨")

label1.pack()
label2.pack()
entry1.pack()
entry2.pack()
button1.pack()
button2.pack()


window.mainloop()