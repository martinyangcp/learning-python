import turtle
t=turtle.Turtle()
t.shape("turtle")
x1=int(turtle.textinput("x1 ","입력해라"))
y1=int(turtle.textinput("y1 ","입력해라"))
x2=int(turtle.textinput("x2 ","입력해라"))
y2=int(turtle.textinput("y2 ","입력해라"))
x3=int(turtle.textinput("x3 ","입력해라"))
y3=int(turtle.textinput("y3 ","입력해라"))
t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.goto(x3,y3)
turtle.done()