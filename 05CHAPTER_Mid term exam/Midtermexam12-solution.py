num = int(input("정수를 입력하시오 >> "))

for i in range(num) :
    for j in range(i+1) :
        print('*', end = "")
    print() #<<< 이게 왜들어간거에요?

print("=========================================")

for i in range(num, 0, -1) :
    for j in range(i) :
        print('*', end = "")
    print()

print("=========================================")

for i in range(num) :
    for j in range(num-i) :
        print(" ", end = "")
    for j in range(i+1) :
        print('*', end = "")
    print()

print("=========================================")

for i in range(num, 0, -1) :
    for j in range(num-i) :
        print(" ", end = "")
    for j in range(i) :
        print('*', end = "")
    print()

print("=========================================")

for i in range(num, 0, -1) :
    for j in range(num-i) :
        print(" ", end = "")
    for j in range(i) :
        print('*', end = "")
    print()

print("=========================================")

for i in range(1, num + 1, 2) :
    for j in range((num - i) //2) :
        print(" ", end="")
    for j in range(i) :
        print("*", end="")
    print()
for i in range(num, 1, -2) :
    for j in range((num-i )// 2) :
        print(" ", end="")
    for j in range(i - 1) :
        print("*", end="")
    print()
    