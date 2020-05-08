score=int(input("성적을 입력하시오 :"))
if 0 <= score and score <= 100:
    if score >= 90 :
        print("A학점입니다.")
    elif score>=80:
        print("B학점입니다.")
    elif score>=70:
        print("C학점입니다.")
    elif score>=60:
        print("D학점입니다.")
    else:
        print("F학접입니다.")
else :
    print("성적의 영역을 잘 못 입력하셨습니다.")