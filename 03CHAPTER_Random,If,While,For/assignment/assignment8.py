import turtle
t=turtle.Turtle()
t.shape("turtle")

for num in range (50):
    t.forward(250)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(250)
    t.left(90)
    t.forward(30)
    t.left(90)

turtle.done()
