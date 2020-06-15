slist=[]

def list_sort() :
    global slist                                # 4, 3, 2, 1, 5

    for _ in range(len(slist)-1) :
        for i in range(len(slist)-1) :          # i = 0 
            if(slist[i] > slist[i+1]) :         # slist[0] > slist[1]
                temp = slist[i]                 # temp = slist[0]       (temp = 5)
                slist[i] = slist[i+1]           # slist[0] = slist[1] (slist[0] = 4)
                slist[i+1] = temp               # slist[1] = temp       (slist[1] = 5)

num =int(input("몇 개의 수를 입력받을 건가요?"))

for s in range(1,num+1,1):
    slist.append(int(input(str(s)+"번째 수 :")))

print("입력직후 :" , slist)
list_sort()
print("배열된 후 :", slist)

