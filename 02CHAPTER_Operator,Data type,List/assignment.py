import turtle
t=turtle.Turtle()
t.shape("turtle")
c1=turtle.textinput("터틀터틀","첫번째 색")
c2=turtle.textinput("터틀터틀","두번째 색")
c3=turtle.textinput("터틀터틀","세번째 색")
c4=turtle.textinput("터틀터틀","네번째 색")

t.fillcolor(c1)
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(30,0)
t.down()

t.fillcolor(c2)
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(60,0)
t.down()

t.fillcolor(c3)
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(90,0)
t.down()

t.fillcolor(c4)
t.begin_fill()
t.circle(50)
t.end_fill()
turtle.done()
