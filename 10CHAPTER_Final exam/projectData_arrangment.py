from datetime import datetime

'''
학생의 정보를 자동 정리하고 해당 학생들의 성적을 평균내는 프로그램 입니다.

<프로그램 전>
Sam	27      A  B C  A  B
	Lee        18	A A  B  C  A
Kim    30 	B  C D  B   B
  Pack	28	C   C A D  A
 Lim	   	21	D  C  D  A B
  Jeong     22	B A   C  B A
Kang		20      B  B  C  C A

<프로그램 후>
Name    Age    Subject  Average
Sam	    27	  A	B	C	A	B	3.2	
Lee	    18	  A	A	B	C	A	3.4	
Kim	    30	  B	C	D	B	B	2.4	
Pack	  28	  C	C	A	D	A	2.6	
Lim	    21	  D	C	D	A	B	2.2	
Jeong	  22	  B	A	C	B	A	3.2	
Kang	  20	  B	B	C	C	A	2.8	

Total Average : 2.83    (June 22, 2020)
'''
# A 4.0, B 3.0, C 2.0, D 1.0, F 0.0

def readwrite(infile, outfile):
    infile = open(infile,"r")
    content = []
    outfile = open(outfile,"w")
   

    for line in infile:
      line = line.rstrip()
      data = line.split()
      content.append(data)
      
    outfile.write("Name    Age                   Subject                 Average")
    total_avg = 0
    total_person = 0
    for i in content: #"\n", "\t", "\b"
      sum = 0
      outfile.write("\n")

      for j in i :
        
        if j == "A":
          sum += 4
        elif j == "B":
          sum += 3
        elif j == "C":
          sum += 2
        elif j == "D":
          sum += 1
        

        outfile.write(j + "\t")
      outfile.write(str(sum/5))
      total_avg += sum/5
      total_person += 1
  
    infile.close()
    nowdate = datetime.now()
    outfile.write("\n")
    outfile.write("Total Average :"+str(total_avg/total_person)+"\t(" + nowdate.strftime("%B ") + nowdate.strftime("%d") + "," + nowdate.strftime("%Y") + ")")

    



readwrite("students.txt", "student_avg.txt")


