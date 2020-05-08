import turtle
t=turtle.Turtle()
t.shape("turtle")

X=int(turtle.textinput("터틀터틀","큰 원 x좌표"))
Y=int(turtle.textinput("터틀터틀","큰 원 y좌표"))
x=int(turtle.textinput("터틀터틀","작은 원 x좌표"))
y=int(turtle.textinput("터틀터틀","작은 원 y좌표"))
R=int(turtle.textinput("터틀터틀","큰 원 반지름"))
r=int(turtle.textinput("터틀터틀","작은 원 반지름"))

t.up()
t.goto(X,Y)
t.down()
t.circle(R)
t.up()
t.goto(x,y)
t.down()
t.circle(r)

if (((X-x)**2+(Y-y)**2)**0.5) > R+r :
    t.write("작은 원이 큰 원 외부에 있습니다.")
elif  (((X-x)**2+(Y-y)**2)**0.5) == R+r :
    t.write("작은 원이 큰 원과 맞닿아 있다")
else :
    t.write("작은 원이 큰 원 내부에 있다.")
        

turtle.done()
