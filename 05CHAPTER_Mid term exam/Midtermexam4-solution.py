max_num = 0
num_list = []

for i in range(10) :
    num = int(input(str(i + 1) + "번째 숫자를 입력하시오 >> "))
    num_list.append(num)

    if num > max_num :
        max_num = num

min_num = max_num

for i in range(10) :
    if num_list[i] < min_num :
        min_num = num_list[i]

print("입력된 값은 " + str(num_list) + "이며,")
print("제일 큰 값은 " + str(max_num) + "이고,")
print("제일 작은 값은 " + str(min_num) + "이다.")