import datetime

"""
Using OOP principles that you have learned such as classes, objects, instance methods and encapsulation make different bank account objects that belong to different classes:

- chequing account
- savings account
- students account

Think of some attributes and methods that each unique bank account will need for example:

- monthly charges
- monthly/yearly interest on savings
- maximum transactions
- minimum account balance
"""

"""
For the sake of displaying a currency, the currency will be displayed as '£'
"""

class CheckingAccount:
    def __init__(self, accountHolder, accountNumber, accountBalance=0.0):
        time = datetime.datetime.now()
        self.accountHolder = accountHolder
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance
        self.statement = [f'Account started @ {time.strftime("%c")}. Balance: £{self.accountBalance}']

    def deposit(self, amount):
        time = datetime.datetime.now()
        self.accountBalance = (self.accountBalance + amount)
        self.statement.append(f'Deposited £{amount} @ {time.strftime("%c")}. Balance: £{self.accountBalance}')
        return (f"You deposited £{amount} and your new balance is £{self.accountBalance}.")

    def withdraw(self, amount):
        if self.accountBalance <= 0 or self.accountBalance < amount:
            return (f"You have insufficient funds to withdraw £{amount}.\nYou only have £{self.accountBalance} and will need to deposit more funds.")
        else:
            time = datetime.datetime.now()
            self.accountBalance = (self.accountBalance - amount)
            self.statement.append(f'Withdrew £{amount} @ {time.strftime("%c")}. Balance: £{self.accountBalance}')
            return (f"You withdrew £{amount} and your new balance is £{self.accountBalance}.")

    def checkBalance(self):
        return (f"Your current balance is £{self.accountBalance}.")

    def checkStatement(self):
        for i in range(len(self.statement)):
            print(self.statement[i])            


class SavingsAccount(CheckingAccount):
    def __init__(self, accountHolder, accountNumber, accountBalance=0.0, monthCharges={}):
        super().__init__(accountHolder,accountNumber,accountBalance)
        self.accountHolder = accountHolder
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance
        self.monthCharges = monthCharges
        self.interestRate = 0.67

    def addMonthCharge(self, vendor, amount):
        self.monthCharges[vendor] = amount
        return (f'A new monthly charge has been setup for {vendor} at £{amount}.\nAll current vendor charges are: {self.monthCharges}')

    def chargeAccount(self):
        charges = self.monthCharges.values()
        totalCharge = sum(charges)
        if self.accountBalance < totalCharge:
            return (f'You have insufficient funds to keep your monthly outgoings and risk going into debt.\nTotal monthly outgoings is: £{totalCharge}\nYour current balance is: £{self.accountBalance}')
        else:
            time = datetime.datetime.now()
            self.accountBalance = (self.accountBalance - totalCharge)
            self.statement.append(f'Monthly total charge: £{totalCharge} @ {time.strftime("%c")}. Balance: £{self.accountBalance}')
            return (f"Monthly total charge £{totalCharge} has been debited and your new balance is £{self.accountBalance}.")

    def interestAdd(self, month_or_year):
        if month_or_year.lower() == "month":
            self.accountBalance = self.accountBalance + ((self.accountBalance / 100) * self.interestRate)
            return (f'Monthly interest of {self.interestRate} was added to your account.\nYour balance is now £{self.accountBalance}.')
        elif month_or_year.lower() == "year":
            self.accountBalance = self.accountBalance + (((self.accountBalance / 100) * self.interestRate) * 12)
            return (f'Yearly interest of {self.interestRate * 12} was added to your account.\nYour balance is now £{self.accountBalance}.')
        else:
            return (f'{month_or_year} is not recognised as a command. Use "month" or "year".')


class StudentAccount(SavingsAccount):
     
    def __init__(self, accountHolder, accountNumber, accountBalance=0.0, monthCharges={}, age=16):
        super().__init__(accountHolder,accountNumber,accountBalance, monthCharges)
        self.age = age
        self.maxLimit = 50

    def addMonthCharge(self, vendor, amount):
        if self.age < 18 and amount > self.maxLimit:
            return (f'You are currently restricted to single transactions of £{self.maxLimit}.')
        else:
            self.monthCharges[vendor] = amount
            return (f'A new monthly charge has been setup for {vendor} at £{amount}.\nAll current vendor charges are: {self.monthCharges}.')
        
    def withdraw(self, amount):
        if self.age < 18 and amount > self.maxLimit:
            return (f'You are currently restricted to single transactions of £{self.maxLimit}.')
        else:
            if self.accountBalance <= 0 or self.accountBalance < amount:
                return (f"You have insufficient funds to withdraw £{amount}.\nYou only have £{self.accountBalance} and will need to deposit more funds.")
            else:
                time = datetime.datetime.now()
                self.accountBalance = (self.accountBalance - amount)
                self.statement.append(f'Withdrew £{amount} @ {time.strftime("%c")}. Balance: £{self.accountBalance}')
                return (f"You withdrew £{amount} and your new balance is £{self.accountBalance}.")


myAccount = StudentAccount(
    accountHolder = "Christoph Waltz", accountNumber="0987", age=18
)

print(myAccount.deposit(2000))
print(myAccount.withdraw(51))

print(myAccount.interestAdd("Month"))

print(myAccount.addMonthCharge("Tesla Finance", 200.0))
print(myAccount.addMonthCharge("BT", 50.0))
print(myAccount.addMonthCharge("FreeTrade", 100.0))

print(myAccount.chargeAccount())

myAccount.checkStatement()