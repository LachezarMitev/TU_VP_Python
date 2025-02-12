class Building:
    def __init__(self, height: int, area: float, address: str):
        self.Height = height
        self.Area = area
        self.Address = address
    
    def Print(self):
        print(f"h: {self.Height}m.; S: {self.Area}sq.m.; Address: {self.Address}")
    
class House(Building):
    def __init__(self, height: int, area: float, address: str, floors: int, owner: str):
        super().__init__(height, area, address)
        self.Floors = floors
        self.Owner = owner

    def Print(self):
        super().Print()
        print(f"Floors; {self.Floors}; Owner: {self.Owner}")

def Largest(houses: list[House]):
    l = 0
    lh = House
    for h in houses:
        if h.Height / h.Floors > l: 
            l == h.Height / h.Floors
            lh = h
    return lh

h1 = House(10, 10, "a", 2, "q")
h2 = House(10, 10, "a", 5, "q")

l = [h1, h2]
print(Largest(l).Area)