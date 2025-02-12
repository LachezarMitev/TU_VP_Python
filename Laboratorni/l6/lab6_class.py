class Person:
    def __init__(self, fnam, lnam, age):
        self.Fnam = fnam
        self.Lnam = lnam
        self.Age = age
        self.__dSize = 0.1 #privete type shi
        self._mazna = "dimoff" #protected type shi
    def BasicInfo(self):
        print(self.Fnam, self.Lnam, self.Age)

class Employee(Person):
    def __init__(self, fnam, lnam, age, salary):
        super().__init__(fnam, lnam, age)
        self.Fnam = fnam
        self.Lnam = lnam
        self.Age = age
        self.Salary = salary
    def EmplInfo(self):
        super().BasicInfo() #izvikva func ot parent class
        print(self.Salary, "bgn.", self._mazna)

# a = Person("Georgi", "Ignatov", 40)
# print(a.Fnam)
# print(a.Lnam)
# a.BasicInfo()

emp = Employee("Georgi", "Ignatov", 40, 50000)
emp.BasicInfo()
emp.EmplInfo()
del emp.Age
emp.Age = 30
print(emp.Age)


class aaa:
    @staticmethod #static method type shi
    def Method():
        print("aaaaaa")

# aaa.Method()