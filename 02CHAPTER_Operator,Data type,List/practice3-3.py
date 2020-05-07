import turtle
t = turtle.Turtle()
a = turtle.textinput("입력창 제목","이름???")
for num in range(4):
    t.forward(100)
    t.left(90)
t.write("안녕하세요 " + a + "씨, 터틀 인사드립니다.")
turtle.done()