from tkinter import *
from PIL import ImageTk,Image                        # RGB 3차원의 값

def change_img():
    path = inputBox.get()                            # entry 값
    img = ImageTk.PhotoImage(Image.open(path))       # 새로운 파일의 경로
    imageLabel.configure(image = img)                # id에 값을 설정
    imageLabel.image = img                           # label에 새로 그림

window = Tk()

photo = ImageTk.PhotoImage(Image.open("wl.gif"))     # 파일의 상대경로
imageLabel = Label(window,image = photo)             # label에 그림
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window,text = "submit", command = change_img)
button.pack()

window.mainloop()