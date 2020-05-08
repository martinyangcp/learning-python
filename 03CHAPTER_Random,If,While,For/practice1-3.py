import random
first=random.randint(1,100)
second=random.randint(1,100)
answer=int(input(str(first)+"-"+str(second)+"="))
if answer == first-second :
    print("맞았습니다.")
else:
    print("틀렸습니다.")
