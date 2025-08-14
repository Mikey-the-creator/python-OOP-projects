from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []  # Store all transaction records

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__record_transaction("Deposit", amount)
            return f"Deposited ₦{amount}. New balance: ₦{self.__balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            self.__record_transaction("Withdrawal", amount)
            return f"Withdrew ₦{amount}. New balance: ₦{self.__balance}"
        return "Insufficient funds or invalid amount."

    def apply_interest(self, rate_percent):
        if rate_percent > 0:
            interest = self.__balance * (rate_percent / 100)
            self.__balance += interest
            self.__record_transaction("Interest", interest)
            return f"Applied {rate_percent}% interest. New balance: ₦{self.__balance}"
        return "Interest rate must be positive."

    def transfer(self, target_account, amount):
        if self.withdraw(amount) != "Insufficient funds or invalid amount.":
            target_account.deposit(amount)
            self.__record_transaction(f"Transfer to {target_account.get_owner()}", amount)
            return f"Transferred ₦{amount} to {target_account.get_owner()}"
        return "Transfer failed. Check your balance."

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def get_transaction_history(self):
        return self.__transactions

    def __record_transaction(self, transaction_type, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transactions.append({
            "type": transaction_type,
            "amount": amount,
            "balance_after": self.__balance,
            "time": timestamp
        })
