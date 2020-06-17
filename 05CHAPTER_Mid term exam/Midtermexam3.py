st=int(input("시작 수 : " ))
fin=int(input("끝 수 : " ))
jung=int(input("증가 값 : "))


add = 0 
mul = 1

for i in range (st,fin+1,jung):
    add +=i
    mul *=i


print("="*85)

print("합 :", end = "")
for i in range(st,fin,jung) :
    print(i, "+", end = "")
print(fin, "=" , add)



print("곱 : ",end = "")
for i in range(st,fin,jung):
    print(i,"*",end = "")
print(fin,"=",mul)
print("="*85)


