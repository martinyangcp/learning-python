Power = False    # 전원 : false - off, true - on
Volume = 10      # 볼륨 : 1 ~ 20
Channel = 1      # 채널 : 1 ~ 10

def power() :
    global Power
    
    if Power == False :
        Power = True
        print("| 전원을 켰습니다. |")
    else :
        Power = False
        print("| 전원을 껐습니다. |")

def setVolumnUp(size) :
    global Volume
    Volume += size

    if Volume < 1 :
        Volume = 1

def setVolumnDown(size) :
    global Volume
    Volume -= size

    if Volume > 20 :
        Volume = 20

def setChannelUp(size) : 
    global Channel
    Channel += size

    if Channel < 1 :
        Channel = 1
        
def setChannelDown(size) : 
    global Channel
    Channel -= size

    if Channel > 10 :
        Channel = 10

def getNow() :
    print("==========================")
    print("현재의 상태를 출력합니다.")
    print("TV의 전원 : ")

    if Power == True :
        print("켜져있습니다.")
    else :
        print("꺼져있습니다.")
    
    print("TV의 볼륨 : " + str(Volume))
    print("TV의 채널 : " + str(Channel))
    print("==========================")

while True :
    print("======================================")
    print("1. 전원 끄기")
    print("2. 전원 켜기")
    print("3. 볼륨 조절")
    print("4. 채널 조절")
    print("5. 현재의 상태 출력")
    print("6. 프로그램 종료")
    print("======================================")

    order = int(input("원하는 기능의 번호를 입력하세요 >> "))

    if order == 1:
        if Power == False :
            print("이미 꺼져있습니다.")
        else :
            power()
    elif order == 2 :
        if Power == True :
            print("이미 켜져있습니다.")
        else :
            power()
    elif order == 3 :
        if Power == False :
            print("TV가 꺼져있습니다.")
        else :
            size = int(input("볼륨을 조정합니다 :: 범위 1~20\n조절하고자 하는 값을 입력하세요 >> "))

            if size > 0 :
                setVolumnUp(size)
            else :
                setVolumnDown(size * -1)
    elif order == 4 :
        if Power == False :
            print("TV가 꺼져있습니다.")
        else :
            size = int(input("채널을 조정합니다 :: 범위 1~10\n조절하고자 하는 값을 입력하세요 >> "))

            if size > 0 :
                setChannelUp(size)
            else :
                setChannelDown(size * -1)    
    elif order == 5 :
        getNow()
    elif order == 6 :
        print("프로그램을 종료합니다.")
        break
    else :
        print("기능의 번호를 잘 못 누르셨습니다. 범위는 1 ~ 6입니다. ")