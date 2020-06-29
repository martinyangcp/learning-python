import turtle
import random

color = ["yellow", "orange", "white", "red", "purple", "blue"]

t = turtle.Turtle()
t.speed(0)

def drawing(c, leng, sides, x, y):
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor(c)
    t.begin_fill()

    for _ in range(sides) :
        t.forward(leng)
        t.right(360/sides)

    t.end_fill()

for i in range(20) :
    choice_color = random.choice(color)
    length = random.randint(10, 200)
    n = random.randint(3, 6)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    drawing(choice_color, length, n, x, y)



turtle.done()