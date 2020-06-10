import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(5)

def square() :
    for _ in range(4):
        t.forward(100)
        t.left(90)

for num in range(3):
    square()
    t.up()
    t.forward(150)
    t.down()

turtle.done()
