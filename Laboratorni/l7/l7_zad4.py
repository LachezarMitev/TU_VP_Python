class Vehicle:
    def __init__(self, wheels: int, model: str, colour: str):
        self.Wheels = wheels
        self.Model = model
        self.Colour = colour

    @staticmethod
    def Add(w: int, m: str, c: str):
        vh = Vehicle(w, m, c)
        return vh
    def Info(self):
        print(f"Wheels: {self.Wheels}, Model: {self.Model}, Colour: {self.Colour}")
    
class LuxuryCar(Vehicle):
    def __init__(self, wheels: int, model: str, colour: str, passengers: int):
        super().__init__(wheels, model, colour)
        self.Passengers = passengers

    @staticmethod
    def Add(w: int, m: str, c: str, p: int):
        lc = LuxuryCar(w, m, c, p)
        return lc
    def Info(self):
        super().Info()
        print(f"Passengers: {self.Passengers}")

class SportsCar(Vehicle):
    def __init__(self, wheels: int, model: str, colour: str, loadLimit: float):
        super().__init__(wheels, model, colour)
        self.LoadLimit = loadLimit

    @staticmethod
    def Add(w: int, m: str, c: str, ll: float):
        sc = SportsCar(w, m, c, ll)
        return sc
    def Info(self):
        super().Info()
        print(f"Load limit: {self.LoadLimit}")

lc1 = LuxuryCar.Add(4, "e38", "black", 5)
lc2 = LuxuryCar.Add(4, "maybach", "white", 5)
sc1 = SportsCar.Add(4, "g80", "blue", 2000)
sc2 = SportsCar.Add(4, "c63", "green", 1900)
lc1.Info()
lc2.Info()
sc1.Info()
sc2.Info()