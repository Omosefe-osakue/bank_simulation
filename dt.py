class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

def main():
    accounts = {}
    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            if account_number not in accounts:
                initial_balance = float(input("Enter initial balance: $"))
                accounts[account_number] = BankAccount(account_number, initial_balance)
                print("Account created.")
            else:
                print("Account already exists.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter deposit amount: $"))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter withdrawal amount: $"))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account balance: ${balance}")
            else:
                print("Account not found.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
