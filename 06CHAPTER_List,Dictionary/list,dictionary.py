num_list = []           # 리스트
num_dict = {}           # 딕셔너리

num_list = [1, 2, 3, 4] #리스트
           #0  1  2  3
num_dict = {"가": 0, "나": 1}

print(num_list[0])
print(num_dict["가"])

num_dict["다"] = 2
print(num_dict)

for i in range(len(num_list)) :
    print(num_list[i])

for key in num_dict.keys() :
    print(key, num_dict[key])