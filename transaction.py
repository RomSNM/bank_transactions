from datetime import datetime

class Transaction:
    def __init__(self, type, amount, description=""):
        self.type = type
        self.amount = amount
        self.data = datetime.now()
        self.description = description

    def __str__(self):
        return f"[{self.data.strftime('%Y-%m-%d %H:%M:%S')}] {self.type}: ${self.amount:.2f} {self.description}"