import random

'''
프로그램의 조건은 다음과 같습니다. 다음 조건에 알맞는 Up&Down 게임을 만들어봅시다.

1. 사용자에게 최소값과 최대값을 입력 받습니다. (단, 최소값이 최대값보다 작지 않다면 다시 입력받아야 합니다.)
2. 숨겨진 값은 최소값부터 최대값 사이의 랜덤한 하나로 설정합니다.
3. 추측 방식
    - computer는 항상 최소와 최대값의 평균 값으로 추측합니다.
    - 사용자는 항상 숫자를 입력받습니다.
4. 범위를 점차 좁혀가면서, 범위의 범주를 넘으면 "최소값부터 최대값사이의 값을 넣어야한다"는 메시지를 보여줍니다.
5. 누가 이겼는지, 몇번만에 이겼는지도 같이 보여줍니다.
'''
count = 1

while True:
    min = int(input("최소값 :"))  # 최소값
    max = int(input("최대값 :"))  # 최대값

    if min >= max :
        print("다시 입력하시오.")   
    else :
        break

hidden_number = random.randint(min,max)

computerguess = (min+max)//2
userguess = int(input("사용자 추측"))

while True :
    if userguess == hidden_number:
        print(count, "번 만에 유저 승리")
        break
    elif userguess > hidden_number:
        print("down")
        userguess = int(input("사용자 추측"))
        count += 1
        if (userguess > max) or (userguess < min):
            print("최소값부터 최대값사이의 값을 넣어야한다.") 

    elif userguess < hidden_number:
        print("up")
        userguess = int(input("사용자 추측"))
        count += 1

        if (userguess > max) or (userguess < min):
            print("최소값부터 최대값사이의 값을 넣어야한다.") 

    if computerguess == hidden_number:
        print(count, "번 만에 컴퓨터 승리")
        break
    elif computerguess > hidden_number:
        computerguess = (computerguess+min)//2
        
    elif computerguess < hidden_number:
        computerguess = (computerguess+max)//2
        
    


