class Number:
    def __init__(self, val):
        self.Val = val
    def Sqr(self):
        return self.Val ** 2
    def Cube(self):
        return self.Val ** 3
    def Print(self):
        print(f"Num: {self.Val}")

num = Number(int(input()))
print(num.Sqr())
print(num.Cube())
num.Print()
