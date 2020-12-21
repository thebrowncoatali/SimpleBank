


class BankInfo():

    def __init__(self, name, account, balance, rate, deposit, withdrawal):
        self.name = name
        self.account = account
        self.rate = rate
        self.balance = balance
        self.deposit = deposit
        self.withdrawal = withdrawal

    def monthly_balance(self, balance):
        balance += deposit - withdrawal  
        return balance

    def calc_interest(self, balance, rate):
        interest = balance * rate / 1200
        return interest