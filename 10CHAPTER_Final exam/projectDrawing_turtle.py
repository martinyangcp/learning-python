import turtle

colors = ["black", "orange", "red", "purple", "blue", "orchid", "gold"]

def draw(x, y) :
    drag.ondrag(None)        
    message.clear()
    message.hideturtle()
    drag.goto(x, y)
    '''
    이전에서 지금으로 이동했을때 선을 그려주는 코드
    : 기능 - 이동한 방향의 8방향으로 선을 그림
    '''

    temp_x = [1, 1, -1, -1, 1, 1, -1, -1]
    temp_y = [1, -1, 1, -1, 1, -1, 1, -1]

    for i in range(1, number_of_area) :
        if i < 4 :
            new_x = x * temp_x[i]
            new_y = y * temp_y[i]
        else :
            new_x = y * temp_y[i]
            new_y = x * temp_x[i]
        
        drawing[i].goto(new_x, new_y)

    drag.ondrag(draw)

def clearDrawing():
    for i in drawing:
        i.clear()
    
    message.write("지워졌다")
    '''
    그려진 모든 내용을 지우는 코드
    : 기능 - 화면의 turtle이 지워진다
    : message로 "지워졌다"는 알림 문구가 뜸
    '''

def goToMiddle():
    for i in drawing:
        i.up()
        i.goto()
        i.down()

    message.write("중앙으로 이동했다")
    '''
    원이 중앙으로 다시 위치하는 코드
    : 기능 - 화면의 중앙으로 turtle이 이동한다.
    : message로 "중앙으로 이동했다"는 알림 문구가 뜸
    '''


def handleColourChange(x, y) :
    for i in range(len(colors)) :
        if x <= (-130 + 50 * i) :            
            for j in range(number_of_area) :
                drawing[j].color(colors[i])
            break

def changeColour():
    num = turtle.textinput("인덱스 입력")
    if not 1 <= int(num) <= 6:
        num = turtle.textinput("인덱스 재 입력")
    col = turtle.textinput("바꿀 색 입력")
    if col != None:
        num = turtle.textinput("바꿀 색 재 입력")
    colorBox[num]= col
    message.write("색이 정상적으로 바뀌었다")
     
    '''
    원하는 색의 값을 바꾸는 코드
    : 기능 - 인덱스를 받고, 원하는 색의 이름으로 바꿈
    : 단, 범위의 인덱스가 아니거나 유의미한 색의 이름이 아니면 재입력받아야함
    : message로 "색이 정상적으로 바뀌었다."는 알림 문구가 뜸
    '''
    turtle.listen()

turtle.setup(800,600)  
number_of_area = 8  
turtle_width = 3 

turtle.tracer(False)

Lines = turtle.Turtle()

Lines.width(1)

Lines.down()
Lines.color("gray88")

for i in range(number_of_area):
    Lines.forward(500)
    Lines.backward(500)
    Lines.left(360 / number_of_area)

Lines.hideturtle()

message = turtle.Turtle()
message.color("red")
message.up() 
message.goto(0, -200)
message.hideturtle()

drawing = [] 

for _ in range(number_of_area) :
    temp = turtle.Turtle()

    temp.speed(0)
    temp.width(turtle_width)
    temp.hideturtle()

    drawing.append(temp)

drag = drawing[0]
drag.showturtle()
drag.shape("circle")
drag.shapesize(3, 3)

drag.ondrag(draw)

turtle.onkeypress(clearDrawing, "c")    #_________________________________c를 누르면 화면의 내용이 지워짐
#_________________________________m을 누르면 화면의 정중앙으로 turtle이 다시 위치함
#_________________________________s를 누르면 color를 바꿀 수 있음

colorBox = []

for i in range(len(colors)) :
    t = turtle.Turtle()
    t.shape("square")
    t.shapesize(2, 2)
    t.up()
    t.color(colors[i])
    t.goto(-150 + 50 * i, 250)
    colorBox.append(t)
    t.onclick(handleColourChange)
    t.down()

turtle.tracer(True)
turtle.listen()

turtle.done()

