import turtle
import random
t=turtle.Turtle()
t.shape("turtle")
t.speed(10)     # 1 ~ 10, no-animation : 0
# -300, 300
# 10, 100
for _ in range(1000):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    t.up()
    t.goto(x,y)
    t.down()
    r=random.randint(10,100)
    t.circle(r)

turtle.done()