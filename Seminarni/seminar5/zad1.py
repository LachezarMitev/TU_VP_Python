class Nams:
    def __init__(self, l:list[int]):
        self.L = l
    
    def PrintNams(self):
        print(self.L)

    def SumOfNams(self):
        print(sum(self.L))

a = Nams([int(x) for x in input().split()])
a.PrintNams()
a.SumOfNams()