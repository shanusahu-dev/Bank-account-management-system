class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfullly")
   
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} Withdrawn successfully")
        else:
            print("Insufficient balance")
    def show_details(self):
        print("\nAccount Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)

accounts = {}

while True: 
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit Money") 
    print("3. Withdraw Money") 
    print("4. View Account Details")
    print("5. View All Users")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            print("Account already exists..!")
        else:
            name = input("Enter Account Holder Name: ")
            accounts[acc_no] = BankAccount(acc_no, name)
            print("Account created successfully")
    elif choice == '2':
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_no].deposit(amount)
        else:
            print("Account not found")
    elif choice == '3':
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[acc_no].withdraw(amount)
        else:
            print("Account not found")
    elif choice == '4':
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            accounts[acc_no].show_details()
        else:
            print("Account not found")
    elif choice == '5':
        if not accounts:
            print("No user found")
        else:
            print("\n---All Bank Users ---")
            for acc in accounts.values():
                acc.show_details
    elif choice == '6':
        print("Thank you for using Bank System")
        break
    else:
        print("Invalid choice")
