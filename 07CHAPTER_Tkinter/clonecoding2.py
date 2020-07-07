from tkinter import *

mycolor = "blue"                            # 현재 색

def paint(event):                           # b1-motion이 실행될때 실행되는 함수
    x1,y1 = (event.x -1),(event.y+1)   
    x2,y2 = (event.x -1),(event.y +1)
    # 현재 event가 발생한 x,y좌표를 연산한 결과
    canvas.create_oval(x1,y1,x2,y2, fill =mycolor) 

def change_color():                         # change_color를 정의함 mycolor를 변경함
    global mycolor                          # 함수 안에서 변경되는 mycolor가 함수 밖의 mycolor를 변경하게함
    mycolor ="red"                          # mycolor를 red로 변경함

window = Tk()                               # window 창을 연다
canvas = Canvas(window)                     # 그림을 그리는 canvas 위젯을 선언함\
canvas.pack()                               # canvas를 윈도우에 그려준다
canvas.bind("<B1-Motion>",paint)            # B1-Motion(마우스 왼쪽버튼)을 따라서 색칠한다

button = Button(window,text ="빨간색", command =change_color)
# 버튼을 누르면 change.color를 실행시킨다
button.pack()                               # button위젯을 그린다.
window.mainloop()                           # event가 있는지 확인한다
