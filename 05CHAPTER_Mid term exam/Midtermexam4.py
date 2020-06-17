
slist=[]

for num in range(1,11):
    slist.append(int(input(str(num)+"번째 숫자를 입력하시오 >>")))

def arrange() :
    global slist

    for _ in range(9):
        for i in range(9):
            if(slist[i] > slist[i+1]) :
                temp = slist[i]
                slist[i] = slist[i+1]
                slist[i+1] = temp 

print("입력된 값은 ",slist,"이며,")
arrange()
print("제일 큰 값은 "+str(slist[-1])+"이고,")
print("제일 작은 값은"+str(slist[0])+"이다.")


