class Nams:
    def __init__(self, a:int):
        self.A = a

def Function(a):
    instances = []
    num = 1
    for i in range(a):
        instances.append(Nams(num))
        num += 2
    return instances