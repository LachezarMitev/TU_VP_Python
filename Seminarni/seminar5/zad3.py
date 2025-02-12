class Nams:
    def __init__(self, l:list[int]):
        self.L = l
    
def SumLists(a:Nams, b:Nams):
    outputList = []
    if len(a.L) < len(b.L):
        for i in range(len(a.L)):
            outputList.append(a.L[i] + b.L[i])
        for i in range(len(a.L), len(b.L)):
            outputList.append(0)
    else:
        for i in range(len(b.L)):
            outputList.append(b.L[i] + a.L[i])
        for i in range(len(b.L), len(a.L)):
            outputList.append(0)
    return Nams(outputList)

a = Nams([1, 2, 3])
b = Nams([1, 2, 3, 4, 3, 3, 4 ,5])
c = SumLists(a, b)
print(c.L)
