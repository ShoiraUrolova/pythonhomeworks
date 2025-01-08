import json

class Account:
    """Represents an individual bank account."""

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        if amount > 0:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Withdrawal amount must be positive."

    def to_dict(self):
        """Converts account data to dictionary for serialization."""
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
        }

    @staticmethod
    def from_dict(data):
        """Creates an account instance from a dictionary."""
        return Account(data["account_number"], data["name"], data["balance"])


class Bank:
    """Manages multiple accounts in the bank."""

    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            return "Initial deposit must be non-negative."
        account = Account(self.next_account_number, name, initial_deposit)
        self.accounts[self.next_account_number] = account
        self.next_account_number += 1
        self.save_to_file()
        return f"Account created for {name}. Account number: {account.account_number}"

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.to_dict()
        return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self, filename="accounts.txt"):
        """Saves accounts to a file in JSON format."""
        data = {
            "accounts": [account.to_dict() for account in self.accounts.values()],
            "next_account_number": self.next_account_number,
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_file(self, filename="accounts.txt"):
        """Loads accounts from a file."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.accounts = {
                    acc["account_number"]: Account.from_dict(acc)
                    for acc in data["accounts"]
                }
                self.next_account_number = data["next_account_number"]
        except FileNotFoundError:
            print("No existing accounts file found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error decoding the accounts file.")


def main():
    """Command-line interface for the bank application."""
    bank = Bank()
    bank.load_from_file()

    while True:
        print("\n--- Welcome to the Bank Application ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Enter initial deposit amount: "))
                print(bank.create_account(name, initial_deposit))
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            try:
                account_number = int(input("Enter your account number: "))
                print(bank.view_account(account_number))
            except ValueError:
                print("Invalid account number. Please enter a number.")

        elif choice == "3":
            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter deposit amount: "))
                print(bank.deposit(account_number, amount))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        elif choice == "4":
            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter withdrawal amount: "))
                print(bank.withdraw(account_number, amount))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        elif choice == "5":
            print("Thank you for using the bank application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()