powers = 0
Volume = 10
channel = 1


def power():
    if powers == 0:
        powers = 1
    elif powers == 1:
        powers = 0
    
def setVolumnUp(size):
    global Volume
    Volume += size
    if volumn > 20:
        volumn = 20 

def setVolumnDown(size):
    global Volume
    Volume += size
    if volumn < 1:
        volumn = 1

def setChannelUp(size):
    global channel
    channel += chan

def setchanneldown(size):
    global channel
    channel += chan


def getNow():
    print(powers,Volume,channel)


def choicee():
    print("================================")
    print("1. 전원 끄기")
    print("2. 전원 켜기")
    print("3. 볼륨 조절")
    print("4. 채널 조절")
    print("5. 현재의 상태 출력")
    print("6. 프로그램 종료")
    print("================================")
    choice = int(input("원하는 기능의 번호를 입력하세요 >>"))
    return choice


while True :
    choice = choicee()
    if choice == 1:
        if powers == 0:
            print("<이미 꺼져있습니다.>")
        elif powers == 1:
            power()

    elif choice ==2:
        if powers == 1:
            print("<이미 켜져있습니다.>")
        elif powers == 0:
            power()

    elif choice ==3:
        if powers == 0:
            print("<TV가 꺼져있습니다.>")
            choicee()
        elif powers == 1:
            sound = int(input())
            if sound > 0:
                setVolumnUp(sound)
            if sound < 0:
                setVolumnDown(sound)

    elif choice ==4:
        if powers == 0:
            print("<TV가 꺼져있습니다.>")
            choicee()
        elif powers == 1:
            chan = int(input())
            if chan > 0:
                setChannelUp(chan)
            elif chan < 0:
                setchanneldown(chan)
        
    elif choice ==5:
        getNow()

    elif choice ==6:
        print("프로그램을 종료합니다.")
