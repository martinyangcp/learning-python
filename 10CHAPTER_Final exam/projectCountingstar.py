infile = open("test.txt","r")
countingstar = [0 for _ in range(11)]
for line in infile:
      line = line.rstrip()
      data = int(line)
      countingstar[data] += 1
print(countingstar)

for i in range(11):
    print([i], countingstar[i]*"*")

infile.close()