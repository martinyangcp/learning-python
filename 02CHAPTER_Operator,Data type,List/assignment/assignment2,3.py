import math
import turtle
x1=int(input("x1 :"))
y1=int(input("y1 :"))
x2=int(input("x2 :"))
y2=int(input("y2 :"))
print("두점 사이의 거리 - ",math.sqrt(math.pow((x1-x2),2)+(math.pow((y1-y2),2))))
d=math.sqrt(math.pow((x1-x2),2)+(math.pow((y1-y2),2)))
t=turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.left(90)
t.forward(100)
t.left(135)
t.forward(d)
turtle.done()
