from math import pi

class Shape:
    def __init__(self, type:str):
        self.Type = type
    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, type: str, a:int):
        super().__init__(type)
        self.A = a
    def Area(self):
        return self.A * self.A

class Circle(Shape):
    def __init__(self, type: str, r:int):
        super().__init__(type)
        self.R = r
    def Area(self):
        return pi * self.R * self.R
try:
    fig = input()
    a = int(input())
    if fig == "square":
        f = Square(fig, a)
        print(f.Area)
    elif fig == "circle":
        c = Circle(fig, a)
        print(c.Area)
    else:
        print("Not a figure")
except:
    raise Exception("Sth went wrong")
