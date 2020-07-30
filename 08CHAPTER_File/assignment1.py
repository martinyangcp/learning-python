'''
filename = input("파일 이름을 입력하세요 : ")

infile = open(filename)

count = 0

for line in infile:
    line = line.rstrip()
    count += len(line)
    word_line = line.split()

    for word in word_line :
        len(word)

print("파일 안에는 총",count,"개의 글자가 있습니다.")
infile.close()
'''
'''
filename = input("입력 파일 이름 :")
infile = open(filename)
content = infile.read()
outfilename = input("출력 파일 이름 :")

outfile = open(outfilename,"w")
outfile.write(content)

'''
filename = input("입력 파일 이름 :")
infile = open(filename)

filee = infile.read()

char_list = [0 for i in range(26)]
'''
char_list = []
for i in range(26) :
    char_list.append(0)
'''

for j in filee:         # abcdefah
    for i in range(97,123): # 'a'~'z'
        if j == chr(i):
            char_list[i-97]+=1

for i in range(len(char_list)) :
    print(chr(i+97),"=", char_list[i], end="\t")