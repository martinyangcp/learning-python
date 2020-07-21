#주사위 세개를던졌을때 눈의수의합 , 홀과 짝 구하기
import random
slist =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
odd = 0
even = 0
for n in range(10000):
    A = random.randint(1,6) 
    B = random.randint(1,6) 
    C = random.randint(1,6)
    i = A+B+C
    slist[i-3] += 1
    if i %2 == 0:
        even +=1
    else:
        odd +=1


for K in range(0,16):
    J= K+3 
    print(str(J),"-",slist[K])

print("홀수 : ",str(odd/10),"짝수 :",str(even/10))