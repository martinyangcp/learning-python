pie=3.1415

class Circle :
    def __init__(self,radius):
        self.radius = radius
    
    def calcPerimeter(self) :
        return 2*self.radius*pie
    
    def calcArea(self) :
        return self.radius**2 * pie

    def __str__(self):
        msg = "반지름 :" + str(self.radius) + \
                "원의 둘레 :" + str(self.calcPerimeter()) + \
                "원의 면적 :" + str(self.calcArea())
        return msg

myCircle = Circle(100)
print(myCircle.calcArea())