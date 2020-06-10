import turtle

s1=int(input("첫번째 :"))
s2=int(input("두번째 :"))
s3=int(input("세번째 :"))
s4=int(input("네번째 :"))
s5=int(input("다섯번째 :"))
s6=int(input("여섯번째 :"))
s7=int(input("일곱번째 :"))

slist=[s1,s2,s3,s4,s5,s6,s7]
t=turtle.Turtle()
t.color("blue","red")
t.speed(7)
t.begin_fill()
r=50

def graph(num):
    t.left(90)
    t.forward(slist[num])
    t.write(slist[num])
    t.right(90)
    t.forward(r)
    t.right(90)
    t.forward(slist[num])
    t.left(90)


for num in range (0,7,1):       # 0, 1, 2, 3, 4, 5, 6
    graph(num)


t.right(180)
t.forward(7*r)
t.end_fill()
turtle.done()
