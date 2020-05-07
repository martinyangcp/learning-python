import math
import turtle

x1=int(turtle.textinput("터틀터틀","x1 :"))
y1=int(turtle.textinput("터틀터틀","y1 :"))
x2=int(turtle.textinput("터틀터틀","x2 :"))
y2=int(turtle.textinput("터틀터틀","y2 :"))
print("두점 사이의 거리 - ",math.sqrt(math.pow((x1-x2),2)+(math.pow((y1-y2),2))))
d=math.sqrt(math.pow((x1-x2),2)+(math.pow((y1-y2),2)))
t=turtle.Turtle()
t.shape("turtle")
t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.write("점 사이의 길이 ="+str(d)+")")

turtle.done()