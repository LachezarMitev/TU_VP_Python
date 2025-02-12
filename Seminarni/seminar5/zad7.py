from random import randint

class Food:
    def __init__(self, carbs:int, protein:int, fat:int):
        self.Carbs = carbs
        self.Protein = protein
        self.Fat = fat
    
    def calories(self):
        return 4 * self.Carbs + 4 * self.Protein + 9 * self.Fat
    
class Recipe:
    def __init__(self, name:str, ingredients:list[Food]):
        self.Name = name
        self.Ingredients = ingredients
    
    def calories(self):
        cal = 0
        for i in self.Ingredients:
            cal += i.calories()
        return cal
    def __str__(self):
        return self.Name

try:
    custErr = ValueError("Not in range")
    n = int(input())
    if n > 4 and n < 15:
        for i in range(n):
            f1 = Food(randint(1, 100), randint(1, 100), randint(1, 100))
            f2 = Food(randint(1, 100), randint(1, 100), randint(1, 100))
            f3 = Food(randint(1, 100), randint(1, 100), randint(1, 100))
            nam = input()
            rec = Recipe(nam,[f1, f2, f3])
            print(f"name: {rec.__str__()} calories: {rec.calories()}")
    else:
        raise custErr
except:
    raise Exception("ERR")