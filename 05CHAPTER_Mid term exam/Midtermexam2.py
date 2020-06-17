num=int(input("정수를 입력하시오 >>"))

for nu in range(1,num+1,2):

    print(((num-nu)//2)*" ","*"*nu,((num-nu)//2)*" ")

for na in range(num-1,-1,-2):
    print(((num-na)//2)*" ","*"*na,((num-na)//2)*" ")





