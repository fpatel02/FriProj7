# Bank Class

class BankAccount:
    def __init__(self, account_number):
        """Initializes a new BankAccount instance with the given account number and a balance of 0."""
        self.account_number = account_number  # Set the account number
        self.balance = 0  # Initialize balance to 0

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:  # Check if the deposit amount is positive
            self.balance += amount  # Increase the balance by the deposit amount
            print(f"Successfully deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")  # Error message for invalid deposit

    def withdraw(self, amount):
        """Withdraws a specified amount from the account if sufficient funds exist."""
        if 0 < amount <= self.balance:  # Check if the amount is positive and less than or equal to balance
            self.balance -= amount  # Decrease the balance by the withdrawal amount
            print(f"Successfully withdrew ${amount}. New balance: ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")  # Error message for insufficient funds
        else:
            print("Withdrawal amount must be positive.")  # Error message for invalid withdrawal

    def check_balance(self):
        """Returns the current balance of the account."""
        print(f"Current balance: ${self.balance}.")  # Display the current balance


def main():
    """Main function to interact with the bank account."""
    account_number = input("Enter your account number: ")  # Prompt user for account number
    account = BankAccount(account_number)  # Create a new BankAccount instance

    while True:  # Indefinite loop to allow continuous interaction
        print("\nOptions: (a) Deposit, (b) Withdraw, (c) Check Balance, (d) Exit")  # Display options
        choice = input("Choose an option: ").lower()  # Get user choice and convert to lowercase

        if choice == 'a':  # If the user chooses to deposit
            amount = float(input("Enter amount to deposit: "))  # Get deposit amount from user
            account.deposit(amount)  # Call the deposit method
        elif choice == 'b':  # If the user chooses to withdraw
            amount = float(input("Enter amount to withdraw: "))  # Get withdrawal amount from user
            account.withdraw(amount)  # Call the withdraw method
        elif choice == 'c':  # If the user chooses to check balance
            account.check_balance()  # Call the check_balance method
        elif choice == 'd':  # If the user chooses to exit
            print("Thank you for using the bank account system. Goodbye!")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid option. Please choose again.")  # Error message for invalid option

if __name__ == "__main__":
    main()  # Run the main function
