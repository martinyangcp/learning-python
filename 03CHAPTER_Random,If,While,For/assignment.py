import turtle
t=turtle.Turtle()
t.color("blue")
t.shape("turtle")

for num in range(6):

    t.forward(90)
    t.forward(-20)
    t.left(60)
    t.forward(20)
    t.forward(-20)
    t.right(120)
    t.forward(20)
    t.forward(-20)
    t.left(60)
    t.forward(-70)

    t.left(60)

turtle.done()