import turtle               # import 부분

data = [120, 56, 309, 220, 156, 23, 98]  # global 변수 선언

def drawBar(height) :           # 함수 부분
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(180)
    t.forward(40)
    t.end_fill()
                                
t = turtle.Turtle()             # main 부분
t.color('blue')
t.fillcolor('red')

t.pensize(3)

for d in data :
    #t.begin_fill()
    drawBar(d)
    #t.end_fill()