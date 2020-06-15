import turtle


t=turtle.Turtle()
t.shape("turtle")


def turtlegraph(x):
    return  x**2 + 1



t.forward(200)
t.forward(-200)
t.left(90)
t.forward(200)
t.forward(-200)
t.right(90)
for num in range (10000):
    y = 0.01*turtlegraph(num)

    if y<200:
        t.goto(num,y)

turtle.done()







