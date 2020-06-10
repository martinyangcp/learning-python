# print() 자체 함수화
'''
pi = 3.1415926

def circleArea(radius):
    print("반지름이 "+str(radius)+"인 원의 면적 : "+ str(radius**2*pi ))

def circleCircumference(radius):
    print("반지름이 "+str(radius)+"인 원의 둘레 : "+ str(radius*2*pi))

r = float(input("반지름의 값을 입력하세요 :"))
circleArea(r)
circleCircumference(r)
'''
# 기능을 함수화
'''
pi = 3.1415926

def circleArea(radius):
    return radius**2*pi

def circleCircumference(radius):
    return radius*2*pi

r = float(input("반지름의 값을 입력하세요 :"))
print("반지름이 "+str(r)+"인 원의 면적 : "+ str(circleArea(r)))
print("반지름이 "+str(r)+"인 원의 둘레 : "+ str(circleCircumference(r)))
'''
# global 활용해서 함수화

pi = 3.1415926
area = 0
ference = 0

def circleArea(radius):
    global area
    area = radius**2*pi

def circleCircumference(radius):
    global ference
    ference = radius*2*pi

r = float(input("반지름의 값을 입력하세요 : "))
circleArea(r)
circleCircumference(r)
print("반지름이 "+str(r)+"인 원의 면적 : "+ str(area))
print("반지름이 "+str(r)+"인 원의 둘레 : "+ str(ference))

