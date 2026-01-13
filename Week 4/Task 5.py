class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Mansur", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())
