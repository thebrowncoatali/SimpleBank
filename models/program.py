from models.bank import BankInfo


class Program():

	bank_account = None

	def start():
		name = input("Please enter the name of the account holder: ") 
		account = input("Please enter the account number [100 - 1000]: ")
		rate = float(input("Please enter the annual interest rate percentage [> 0%]: "))
		balance = float(input("Please enter the initial balance [> 100]: "))
		deposit = float(input("Please enter the monthly deposit [> 100]: "))
		withdrawal = float(input("Please enter the monthly withdrawal [< 1000]: "))

		interest = 0

		message = f"""
		Programming Principles Bank Statement

		Account Number: {account}
		Name: {name}
		Initial Balance: {balance}

		"""
		print(message)

		self.bank_account = BankInfo(name, account, balance, rate, deposit, withdrawal)

		for month in range(12):
			balance = newAccount.monthly_balance(balance)
			interest += newAccount.calc_interest(balance, rate)
			print('Month {}'.format(month+1))
			print('Balance: {:.1f}'.format(balance))
			print('Estimated Interest: {:.2f}'.format(interest))
			print("")

		print(balance + interest)
