class Person:
    def __init__(self, fnam, lnam, age, nat):
        self.Fnam = fnam
        self.Lnam = lnam
        self.Age = age
        self.Nat = nat
    def Info(self):
        print(self.Fnam, self.Lnam, self.Age, self.Nat)

class Student(Person):
    def __init__(self, fnam, lnam, age, nat, uni, yearOfStudy):
        super().__init__(fnam, lnam, age, nat)
        
        self.Uni = uni
        self.YearOfStudy = yearOfStudy
    def Info(self):
        super().Info()
        print(self.Uni, self.YearOfStudy)

class Lecturer(Person):
    def __init__(self, fnam, lnam, age, nat, uni, exp):
        super().__init__(fnam, lnam, age, nat)
        
        self.Uni = uni
        self.Experience = exp
    def Info(self):
        super().Info()
        print(self.Uni, self.Experience)

testP1 = Person("Georgi", "Ignatov", 40, "Bg")
testP2 = Person("Ivan", "Ivanov", 20, "Bg")

testS1 = Student("Aleks", "Olimpsa", 40, "Bg", "TU", 2024)
testS2 = Student("Petur", "Petrov", 30, "Bg", "SU", 2020)

testL1 = Lecturer("Ivan", "Dimoff", 19, "Bg", "TU", 19)
testL2 = Lecturer("Georgi", "Georgiev", 50, "Bg", "SU", 20)

testP1.Info()
testP2.Info()

testS1.Info()
testS2.Info()

testL1.Info()
testL2.Info()