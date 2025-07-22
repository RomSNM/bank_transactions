from Account import Checking_Account, Savings_Account


def main():
    """Sample usage of the Bank Account Simulator."""

    # Create checking and savings accounts
    cc = Checking_Account("Romulo", 1)
    cp = Savings_Account("João", 2)

    # ----- Checking account operations -----
    cc.deposit(1000)             # Romulo deposits $1000
    cc.withdraw(300)             # Romulo withdraws $300
    cc.transfer(cp, 200)         # Romulo transfers $200 to João

    # ----- Savings account operations -----
    cp.deposit(500)              # João deposits $500
    cp.simulate_yield(rate=0.01, months=6)  # Simulate 1% monthly yield for 6 months

    # Show transaction history for both accounts
    cc.transaction_history()
    cp.transaction_history()

    # Export transactions to CSV files
    cc.export_transactions_csv("romulo_transactions.csv")
    cp.export_transactions_csv("joao_transactions.csv")


if __name__ == "__main__":
    main()

