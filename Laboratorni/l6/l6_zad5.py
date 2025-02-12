class Aritm:
    def __init__(self, a, b):
        self.A = a
        self.B = b
    def Print(self):
        print(f"A:{self.A}, B:{self.B}")
    def Sum(self):
        return self.A + self.B
    def Diff(self):
        return self.A - self.B
    def Mult(self):
        return self.A * self.B
    def Div(self):
        if self.B != 0:
            return self.A / self.B
        else: return "Error: can't divide wiht 0!"

nums = [int(x) for x in input().split()]
ar = Aritm(nums[0], nums[1])
ar.Print()
print(f"Sum: {ar.Sum()}, Diff: {ar.Diff()}, Mult: {ar.Mult()}, Div: {ar.Div()}")