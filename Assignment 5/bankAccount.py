class Account(object):
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 100
        self.__holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Money Deposited successfully! Current balance : ", self.balance)

    def withdraw(self, amount):
        if (self.balance - amount < 1000):
            print("Sorry, you can't withdraw! your balance becomes less then 1000.")
        else:
            self.balance -= amount
            print("Money withdrawn successfully! Current balance : ", self.balance)

    def displayBalance(self):
        print("Current balance : ", self.balance)

    def displayType(self):
        print("Account can be of Savings or Current type!")

    def transferAmount(self, other, value):
        self.balance -= value
        other.setBalance(other.getBalance() + value)
        print("Money successfully transferred to", other.__holder,
              ". Current balance : ", self.balance)

    def __str__(self):
        return "<<" + "Name:" + str(self.__holder) + ", Current Balance:" + str(self.balance) + ">>"

    @property
    def AccountHolderName(self):
        return self.__holder

    @AccountHolderName.setter
    def AccountHolderNameSet(self, value):
        self.__holder = value

    def setBalance(self, value):
        if value > 0:
            self.balance = value
        else:
            self.balance = 0

    def getBalance(self):
        return self.balance


class Savings(Account):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.type = "Savings"

    def displayType(self):
        print("Account type is : Savings")


acc1 = Account("Tushar")
print(acc1)
print("\nAfter changing the account holder name : ")
acc1.AccountHolderNameSet = "Tushar Gangani"
print()
print(acc1)
print()
acc1.deposit(9000)
acc1.withdraw(4000)
acc1.deposit(500)
acc1.withdraw(1000)
acc1.displayBalance()
acc2 = Account("Tushar 2")
print(acc2)
acc1.transferAmount(acc2, 500)
acc2.displayBalance()
print("Polymorphism : ")
acc3 = Savings("Tushar 3")
acc3.deposit(10000)
acc3.displayType()

