class Nams:
    def __init__(self, txt:str, a:int):
        self.Txt = txt
        self.A = a

def Create(fArg, sArg):
    if type(fArg) == type(sArg) == str:
        return Nams(fArg + sArg, 0)
    elif type(fArg) == type(sArg) == int:
        return Nams("", fArg + sArg)
    else:
        return Nams(fArg, sArg)

a = Create("aa", "bb")
b = Create(1, 2)
c = Create("aa", 1)

print(a.Txt, a.A)
print(b.Txt, b.A)
print(c.Txt, c.A)