class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print("Money deposited.")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print("Money withdrawn.")

        else:
            print("Insufficient balance.")

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount("Ali", 1000)

account.show_balance()

account.deposit(500)

account.withdraw(300)

account.show_balance()