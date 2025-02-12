class BankAccount:
    def __init__(self, accNum: int, owner: str):
        self.AccNum = accNum
        self.Owner = owner
        self.Ballance = 0.0

    def Deposit(self, sum: float):
        self.Ballance += sum
    def Withdraw(self, sum: float):
        if self.Ballance - sum >= 0:
            self.Ballance -= sum
        else:
            print("Insufficient ballance!")
    def DisplayBallance(self):
        print(self.Ballance)

acc1 = BankAccount(1, "joro")
acc2 = BankAccount(2, "pesho")
acc1.Deposit(1234.50)
acc2.Deposit(100.50)
acc1.DisplayBallance()
acc2.DisplayBallance()
acc1.Withdraw(1000)
acc2.Withdraw(1000)
acc1.DisplayBallance()
acc2.DisplayBallance()
