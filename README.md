# 🏦 Python Bank Account Simulator

A simple object-oriented Python project that simulates a bank system with checking and savings accounts. Includes deposit, withdrawal, transfer between accounts, transaction history, yield simulation for savings, and CSV export.

---

## 🚀 Features

- Create checking and savings accounts
- Deposit and withdraw money
- Transfer funds between accounts
- Track transaction history (with timestamps and descriptions)
- Simulate interest yield on savings accounts
- Export transactions to `.csv` files

---

## 📁 Project Structure

```
bank_simulator/
│
├── account.py          # Main classes: Account, Checking_Account, Savings_Account
├── transaction.py      # Transaction class with timestamp, amount, type and description
├── main.py             # Example usage and testing
└── README.md
```

---

## ✅ Technologies

- Python 3
- OOP (Object-Oriented Programming)
- `csv` and `datetime` built-in modules

---

## ▶️ Example

```python
from account import Checking_Account, Savings_Account

cc = Checking_Account("Romulo", 1)
cp = Savings_Account("João", 2)

cc.deposit(1000)
cc.withdraw(300)
cc.transfer(cp, 200)

cc.transaction_history()
cp.transaction_history()

cc.export_transactions_csv("romulo_transactions.csv")
```

---

## 📦 CSV Output Example

```
Data,Type,Amount,Description
2025-07-21 20:30:01,DEPOSIT,1000.00,
2025-07-21 20:32:12,WITHDRAW,300.00,
2025-07-21 20:35:07,TRANSFER OUT,200.00,para 2
```

---

## 📌 Future Improvements

- Exception handling with custom classes (e.g. `SaldoInsuficienteError`)
- Password authentication for accounts
- Data persistence with SQLite or JSON
- CLI or Web interface (Flask or Tkinter)

---

## ✍️ Author

**Romulo Araujo Correa**  
[GitHub Profile](https://github.com/RomSNM)

Project developed to practice Python OOP and strengthen real-world programming logic.
