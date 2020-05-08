import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('red','yellow')
t.begin_fill()

while True:
    t.forward(200)
    t.left(170)

    if abs(t.pos()) < 1 : #이부분 설명해주세요!!
        break

t.end_fill()
turtle.done()
    
    
   