import random

first=random.randint(1,9)
second=random.randint(1,9)

ans=int(input("복권 번호를 입력하시오(10에서 99사이 :"))

if first*10 + second == ans :
    print("상금은 100만원 입니다.")
elif first== ans //10 or second == ans %10 :
    print("상금은 50만원 입니다.")
else :
    print("상금은 없습니다.")








