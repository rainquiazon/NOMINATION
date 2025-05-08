# ATM Simulation in Python (Beginner Version)

# Pre-set account number, PIN, and starting balance
account_number = "12345678"
pin_code = "1234"
balance = 5000  # starting balance in pesos

# Welcome message
print("Welcome to the ATM")

# Ask user for account number
input_account = input("Enter your account number: ")

# Ask user for PIN
input_pin = input("Enter your PIN: ")

# Check if account number and PIN match
if input_account == account_number and input_pin == pin_code:
    print("Authentication successful.\n")
    
    # Keep asking for transactions until the user cancels
    while True:
        # Show transaction options
        print("Please choose a transaction:")
        print("1. Balance Inquiry")
        print("2. Withdraw Cash")
        print("3. Cancel Transaction")
        
        choice = input("Enter choice (1-3): ")  # Get user choice
        
        if choice == "1":
            # Show current balance
            print("\nYour current balance is: ₱", balance)
            
            # Ask if user wants another transaction
            another = input("Do you want another transaction? (yes/no): ")
            if another.lower() != "yes":
                print("Thank you for using the ATM. Goodbye!")
                break  # Exit the loop
                
        elif choice == "2":
            # Ask for withdrawal amount
            while True:
                try:
                    withdraw_amount = float(input("Enter amount to withdraw: ₱"))
                    
                    # Check if amount is less than or equal to balance
                    if withdraw_amount <= balance:
                        print("Processing...\n")
                        
                        # Deduct amount from balance
                        balance -= withdraw_amount
                        
                        # Show receipt
                        print("=== Receipt ===")
                        print("Withdrawn Amount: ₱", withdraw_amount)
                        print("New Balance: ₱", balance)
                        print("================\n")
                        
                        # Ask if user wants another transaction
                        another = input("Do you want another transaction? (yes/no): ")
                        if another.lower() != "yes":
                            print("Thank you for using the ATM. Goodbye!")
                            break  # Exit the inner loop
                        else:
                            break  # Go back to main menu
                    else:
                        # If not enough balance, show message and ask again
                        print("Insufficient balance. Please enter a lower amount.\n")
                except ValueError:
                    # If user types something not a number
                    print("Invalid input. Please enter a number.\n")
        
        elif choice == "3":
            # Cancel transaction
            print("Transaction cancelled. Thank you for using the ATM.")
            break  # Exit the loop

        else:
            # If user types an invalid option
            print("Invalid option. Please try again.\n")

else:
    # If account or PIN is wrong
    print("Authentication failed. Please try again.")
