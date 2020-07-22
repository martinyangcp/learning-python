from tkinter import *
from PIL import ImageTk, Image
import random

computer_choice = "default"
user_choice = "default"


def sscissor():
    global user_choice
    now_Image = ImageTk.PhotoImage(Image.open("scissors.jpg"))
    OutU_I.configure(image = now_Image)
    OutU_I.image = now_Image
    user_choice = "scissors"
    auto_RSP()

def rrock():
    global user_choice
    now_Image = ImageTk.PhotoImage(Image.open("rock.jpg"))
    OutU_I.configure(image = now_Image)
    OutU_I.image = now_Image
    user_choice = "rock"
    auto_RSP()

def ppaper():
    global user_choice
    now_Image = ImageTk.PhotoImage(Image.open("paper.jpg"))
    OutU_I.configure(image = now_Image)
    OutU_I.image = now_Image
    user_choice = "paper"
    auto_RSP()

def auto_RSP():
    global computer_command
    ran = random.randint(0,2)

    if ran == 0 :
        now_Image = ImageTk.PhotoImage(Image.open("rock.jpg"))
        outC_I.configure(image = now_Image)
        outC_I.image = now_Image
        computer_command = "rock"
    elif ran == 1 :
        now_Image = ImageTk.PhotoImage(Image.open("scissors.jpg"))
        outC_I.configure(image = now_Image)
        outC_I.image = now_Image
        computer_command = "scissors"
    elif ran == 2 :
        now_Image = ImageTk.PhotoImage(Image.open("paper.jpg"))
        outC_I.configure(image = now_Image)
        outC_I.image = now_Image
        computer_command = "paper"

    deterwinner()

def deterwinner():
    if computer_choice == user_choice :
        result["text"] = "========="
        showingresult["text"] = "컴퓨터-유저 비김"
    elif (computer_choice == "scissors" and user_choice =="rock") or (computer_choice == "paper" and user_choice =="scissors") or (computer_choice == "rock" and user_choice =="paper"):
        result["text"] = "<<<<<<<<<"
    else :
        result["text"] = ">>>>>>>>>"
        showingresult["text"] = "유저 패"

window = Tk()

computerdec = Label(window, text = "컴퓨터의 결정")
computerdec.grid(row = 0, column = 0)
userdec = Label(window, text = "유저의 결정")
userdec.grid(row =0, column =2)

default_Image = ImageTk.PhotoImage(Image.open("bg.png"))

outC_I = Label(window, image = default_Image, width =200, height = 300)
outC_I.grid(row =1, column = 0)


result = Label(window,text= "", fg= "green", font = "bold", width =30)
result.grid(row = 1, column =1)

OutU_I = Label(window, image = default_Image, width = 200, height = 300)
OutU_I.grid(row = 1,column =2)

showingresult = Label(window, text="", font ="16", fg="green", height = 5)
showingresult.grid(row=2, column=1)

scissor = Button(window,text="가위",command = sscissor)
scissor.grid(row = 3, column = 0)
rock = Button(window,text="바위",command = rrock)
rock.grid(row = 3, column = 1)
paper = Button(window,text="보",command = ppaper)
paper.grid(row =3, column =2)


window.mainloop()