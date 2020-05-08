import turtle
import math
t=turtle.Turtle()
t.color("red")
t.shape("turtle")

for num in range (10):
    t.forward(100)
    t.left(135)
    t.forward(100*(2**0.5))
    t.left(135)
    t.forward(100)
    t.left(80)
    
    
turtle.done()