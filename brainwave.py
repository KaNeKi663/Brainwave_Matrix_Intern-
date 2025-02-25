class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "1234"  # Default PIN for demonstration purposes

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return "PIN changed successfully."
        else:
            return "Incorrect old PIN."

    def authenticate(self, entered_pin):
        return entered_pin == self.pin


def main():
    atm = ATM()
    print("Welcome to the ATM Interface")

    # Authenticate user
    entered_pin = input("Enter your PIN: ")
    if not atm.authenticate(entered_pin):
        print("Incorrect PIN. Exiting...")
        return

    while True:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your current balance is: ${atm.check_balance()}")

        elif choice == "2":
            amount = float(input("Enter the amount to deposit: $"))
            print(atm.deposit(amount))

        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: $"))
            print(atm.withdraw(amount))

        elif choice == "4":
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            print(atm.change_pin(old_pin, new_pin))

        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()