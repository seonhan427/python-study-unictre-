class Shape:
    def  __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, ver, hor):
        super().__init__(x, y)
        self.vertical = ver
        self.horizental = hor
    def area(self):
        return self.vertical * self.vertical
    
    def perimeter(self):
        return 2*self.vertical + 2*self.horizental

rect = Rectangle(0,0,100,200)
print("사각형의 면적:",rect.area())
print("사각형의 둘레:",rect.perimeter())