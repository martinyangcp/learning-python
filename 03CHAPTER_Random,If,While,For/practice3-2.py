import random

while True:
    first=random.randint(1,10)
    second=random.randint(1,10)

    result=int(input(str(first)+"*"+str(second)+"는"))

    if result == first*second:
        print("맞았습니다.")
        break 