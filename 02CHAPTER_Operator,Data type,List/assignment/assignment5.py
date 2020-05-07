import time
t=time.time()

clock=(t//3600)%24
m=(t%60)%60

print("현재시간(영국 그리니치 시각) :",int(clock),"시",int(m),"분" )
