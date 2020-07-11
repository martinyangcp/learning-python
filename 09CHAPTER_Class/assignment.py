from turtle import *
import turtle

class Myturtle(turtle.Turtle) :
    def move(self):
        while True:
            self.forward(100)
            self.right(90)
            



t1 = Myturtle()
t1.move()

turtle.done()
