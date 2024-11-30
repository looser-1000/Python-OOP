# Abstraction: Hiding the implementation details of a class and only showing
#              essential details to the user

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("The car is started...")

car1 = Car()
print(car1.start())


# Encapsulation: Wrapping data and method into a single unit(object).

# Practice Task:
# create a class Account and add two attributes namely account_no and balance
# create method for debit and credit and also calculate balance

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def calculate(self, string, amount):
        if string.lower() == "debit":
            current_balance = float(self.balance - amount)
            print("Your current balance is: " + str(current_balance))
            self.balance = current_balance
        elif string.lower() == "credit":
            current_balance = float(self.balance + amount)
            print("Your Current balance is: " + str(current_balance))
            self.balance = current_balance


account1 = Account(1001, 10000)
print(account1.calculate("debit", 200))
print(account1.calculate("credit", 500))





