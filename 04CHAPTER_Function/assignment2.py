import turtle
t=turtle.Turtle()
t.shape("turtle")
r= 100

def draw_hexa(r):
    for _ in range(6):
        t.forward(r)
        t.left(60)

for _ in range(6):
    t.forward(r)
    t.right(60)
    draw_hexa(r)



    '''
draw_hexa(r)

t.forward(r)
t.left(60)
t.forward(r)
t.right(60)

draw_hexa(r)
t.forward(r)
t.right(60)
t.forward(r)

t.left(60)
draw_hexa(r)

'''







