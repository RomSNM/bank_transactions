from transaction import Transaction
import csv

class Account:

    def __init__(self,holder,number):
        self.holder = holder
        self.balance = 0.0
        self.number = number
        self.transactions = []


    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("DEPOSIT",amount))
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("SAQUE",amount))
        else:
            print("Insufficient balance")


    def extract(self):
        print(f"\n--- Statement for {self.holder} ---")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance: ${self.balance: .2f}")

    def transfer(self, destination_account, amount):
        if not isinstance(destination_account, Account):
            raise TypeError("Destination must be an Account.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        # débito
        self.balance -= amount
        self.transactions.append(
            Transaction("TRANSFER OUT", amount, f"para {destination_account.number}")
        )

        # crédito
        destination_account.balance += amount
        destination_account.transactions.append(
            Transaction("TRANSFER IN", amount, f"de {self.number}")
        )

    def transaction_history(self):
        print(f"\n--- Account transaction history: {self.number} ({self.holder}) ---")

        if not self.transactions:
            print("No transaction registered.")
            return

        for transaction in self.transactions:
            print(transaction)

        print(f"Actual balance: ${self.balance:.2f}")

    def export_transactions_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # header
            writer.writerow(['Data', 'Type', 'Amount', 'Description'])

            for t in self.transactions:
                writer.writerow([
                    t.data.strftime('%Y-%m-%d %H:%M:%S'),
                    t.type,
                    f"{t.amount:.2f}",
                    t.description
                ])

        print(f"Transactions successfully exported to file: {filename}")


class Checking_Account(Account):
    pass

class Savings_Account(Account):
    def simulate_yield(self,rate,months):
        projected = self.balance * ((1 + rate) ** months)
        print(f"Projected balance after {months} months: ${projected:.2f}")


