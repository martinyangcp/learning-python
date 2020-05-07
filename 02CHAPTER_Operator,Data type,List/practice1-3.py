
num=int(input("정수를 입력하시오 : "))
a=num//1000
b=(num-1000*a)//100
c=(num-1000*a-100*b)//10
d=(num-1000*a-100*b-10*c)
answer=a+b+c+d
print("자리 수의 합 :",answer)
'''
num = int(input("정수를 입력하시오 : "))

result = 0

result += num // 1000
num = num % 1000

result += num // 100
num = num % 100

result += num // 10
num = num % 10

result += num
print("자리 수의 합 : ", result)
'''