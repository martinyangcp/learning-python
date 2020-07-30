import turtle

colors = ["black", "orange", "red", "purple", "blue", "orchid", "gold"]

def draw(x, y) :
    drag.ondrag(None)        
    message.clear()
    message.hideturtle()
    drag.goto(x, y)

    x_transform = [1, 1, -1, -1, 1, 1, -1, -1] 
    y_transform = [1, -1, 1, -1, 1,- 1, 1, -1] 

    for i in range(1, number_of_area) : # 1~7(7개)
        if i < 4 :
            new_x = x * x_transform[i]
            new_y = y * y_transform[i]
        else :
            new_x = y * y_transform[i]
            new_y = x * x_transform[i]

        drawing[i].goto(new_x, new_y)

    drag.ondrag(draw)

def clearDrawing():
    for drag in drawing :
        drag.clear()

    message.clear() 
    message.write("그린 내용이 지워짐", align="center", font=("Arial", 14, "bold"))

def goToMiddle():
    for drag in drawing :
        drag.up()
        drag.goto(0, 0)
        drag.down()

    message.clear() 
    message.write("중앙으로 이동함", align="center", font=("Arial", 14, "bold"))

def handleColourChange(x, y) :
    for i in range(len(colors)) :
        if x <= (-130 + 50 * i) :            
            for j in range(number_of_area) :
                drawing[j].color(colors[i])
            break

def changeColour():
    check = True
    changeIndex = turtle.textinput("색 바꾸기", "원해는 0~6사이의 값을 입력하시오.")

    if changeIndex != None :
        changeIndex = int(changeIndex)

        while changeIndex < 0 or changeIndex >= len(colors):
            changeIndex = turtle.textinput("색 바꾸기", "0~6사이의 값만 넣을수있습니다.")

            if changeIndex == None :
                check = False
                break

            changeIndex = int(changeIndex)

        if check : 
            changeColorName = turtle.textinput("색 바꾸기", "색의 이름을 입력하세요.")
            
            if changeColorName != None :
                colors[changeIndex] = changeColorName     
                colorBox[changeIndex].color(changeColorName)   
                        
                message.clear()
                message.write("The colour for that button has been changed, click on the button to use it", align="center", font=("Arial", 14, "bold"))

    turtle.listen()

turtle.setup(800,600)       # window size (width, height)
number_of_area = 8          # turtle area
turtle_width = 3            # drawing size

turtle.tracer(False)        # animation

# Line dawing
Lines = turtle.Turtle()     # (0,0)

Lines.width(1)
Lines.color("gray88")

for i in range(number_of_area):
    Lines.forward(500)
    Lines.backward(500)
    Lines.left(360 / number_of_area)

Lines.hideturtle()

# message dawing
message = turtle.Turtle()   # (0,0)
message.color("red")
message.up() 
message.goto(0, -200)
message.hideturtle()

# turtle list
drawing = [] 

for _ in range(number_of_area) :
    temp = turtle.Turtle()  # (0,0)

    temp.speed(0)
    temp.width(turtle_width)
    temp.hideturtle()

    drawing.append(temp)

drag = drawing[0]
drag.showturtle()
drag.shape("circle")
drag.shapesize(3, 3)

drag.ondrag(draw)                       # draw
turtle.onkeypress(clearDrawing, 'c')    # c 키보드를 누르면 clearDrawing가 실행됨
turtle.onkeypress(goToMiddle, 'm')
turtle.onkeypress(changeColour, 's')

# color Button
colorBox = []

for i in range(len(colors)) :
    t = turtle.Turtle()                 # (0,0)
    t.shape("square")
    t.shapesize(2, 2)
    t.up()
    t.color(colors[i])
    t.goto(-150 + 50 * i, 250)
    colorBox.append(t)
    t.onclick(handleColourChange)       # click - color
    t.down()

turtle.tracer(True)
turtle.listen()                         # event 

turtle.done()