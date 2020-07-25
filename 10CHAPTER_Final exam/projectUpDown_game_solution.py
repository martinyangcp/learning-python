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

finished = False
count = 0

while True :
    lower = int(input("최소값을 입력해주세요 : "))
    upper = int(input("최대값을 입력해주세요 : "))

    if lower > upper :
        print("최소값이 최대값보다 큽니다. 다시 입력하세요.")
    elif lower <= upper :
        print("숨겨진 값의 범위가 제대로 배치되었습니다.")
        break

target = random.randint(lower, upper)

while not finished:             # game - 직접적인 연관
    computer_guess = int((lower + upper) / 2)
    
    player_guess = int(input("접속자가 확인하고자 하는 숫자를 입력하세요 : "))

    if player_guess < lower or player_guess > upper:
        print("숫자 입력은", lower, "부터", upper, "사이의 값만 넣으셔야합니다.")
    elif player_guess > target:
        print("현재 입력 값은 숨겨진 값보다 큽니다.")
    elif player_guess < target:
        print("현재 입력 값은 숨겨진 값보다 작습니다.")
    else:
        finished = True

    if computer_guess > target:
        upper = computer_guess - 1
    elif computer_guess < target:
        lower = computer_guess + 1
    else:
        finished = True

    count = count + 1
    
    print("컴퓨터는", computer_guess, "라고 선택했으며 접속자는", player_guess, "라고 선택했습니다.")
    print("=" * 50)
    
if computer_guess != target:
    print("접속자가 이겼습니다! ", count, "번 만에 맞추셨군요!")
elif player_guess != target:
    print("컴퓨터가 이겼습니다!", count, "번 만에 맞췄습니다!")
else:
    print("접속자와 컴퓨터가 동시에 맞췄습니다. 총", count, "번 걸렸네요.")