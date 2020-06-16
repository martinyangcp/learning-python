add = 0
mul = 1

start = int(input("시작 수 : "))
end = int(input("끝 수 : "))
step = int(input("증가 값 : "))

for i in range(start, end + 1, step) :
    add += i
    mul *= i

print("==========================================")
print("합 : " , end = "")

for i in range(start, end + 1, step) :
    print(str(i) + " + ", end = "")

print("\b\b= " + str(add))
print("곱 : ", end = "")

for i in range(start, end + 1, step) :
    print(str(i) + " * ", end = "")

print("\b\b= " + str(mul))
print("==========================================")