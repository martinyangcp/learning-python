import turtle
import math
t=turtle.Turtle()
t.shape("turtle")

for num in range(360) :
    sin_x = math.sin(math.pi * num / 180.0)
    t.goto(num, sin_x*100)


turtle.done()









