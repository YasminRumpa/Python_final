from abc import ABC, abstractmethod

class Account(ABC):
    accounts={}
    def __init__(self, name, email, address, accountNumber, password, account_type):
        self.name= name
        self.email= email
        self.address= address
        self.type= account_type
        self.balance= 0
        self.accountNo= accountNumber
        self.passW= password
        self.transaction_history= []
        self.loan_cnt= 0
        Account.accounts[self.accountNo] = self 


    def deposit(self,amount):
        if amount>0:
            self.balance+= amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
       if amount>0:
            self.balance-= amount
            self.transaction_history.append(f"withdraw ${amount}")
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
       else:
            print("\nWithdrawal amount exceeded")

    def check_available_balance(self):
           print(f"Available balance: ${self.balance}")
        
    def check_transaction_history(self):
        for transaction in self.transaction_history:
            print(f"Transaction History: {transaction}")
            

    def take_loan(self, amount):
        if self.loan_count<=2:
            self.balance+= amount
            self.loan_cnt+= 1
            self.transaction_history.append(f"Loan amount: ${amount}")
            print(f"Loan amount: ${amount}. New balance: ${self.balance}")
        else:
            print("Highest loan amount reached")

    def transfer(self, target_account, amount):
       if target_account:
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to Account {target_account.accountNo}")
            print(f"Transferred ${amount} to Account {target_account.accountNo}. New balance: ${self.balance}")
        else:
            print("NO balance for the transfer")
       else:
        print("Target account does not exist")

    @abstractmethod
    def showInfo(self):
        pass

class SavingsAccount(Account):
    def __init__(self, name, email, address,accountNumber,password):
        super().__init__(name, email, address, accountNumber,password,"savings")

    def showInfo(self):
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f"\tEmail: {self.email}")
        print(f'\tAddress: {self.address}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')

class CurrentAccount(Account):
    def __init__(self, name, email, address,accountNumber,password):
        super().__init__(name, email, address,accountNumber,password, "current")

    def showInfo(self):
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f"\tEmail: {self.email}")
        print(f"\tAddress: {self.address}")
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')

class Admin:
    def __init__(self):
        self.accounts= {}

    def create_account(self, name, email, address,accountNumber,password, account_type):
        if account_type== "savings":
            account= SavingsAccount(name, email, address,accountNumber,password)
        elif account_type== "current":
            account= CurrentAccount(name, email, address,accountNumber,password)
        self.accounts[accountNumber] = account
        print(f"Account has been successfully created your Account Number: {account.accountNo}")

    def delete_account(self, accountNo):
        if accountNo in self.accounts:
            del self.accounts[accountNo]
            print(f"Account {accountNo} deleted successfully.")
        else:
            print("Account not found")

    def see_accounts(self):
        if self.accounts:
            for accountNo, account in self.accounts.items():
                print(f"Account Number: {accountNo}, Name: {account.name}")
        else:
            print("No user accounts available.")

    def total_available_balance(self, balance):
        total_balance= sum(account.balance for account in self.accounts)
        print(f"Total Available Balance: ${total_balance}")

    def total_loans(self):
        total_loan= sum(account.balance for account in self.accounts if account.loan_cnt> 0)
        print(f"Total Loan: ${total_loan}")

    def turnONloan(self):
        for account in self.accounts:
            account.loan_cnt= 0
        print("No Loan")

    def turnOFFloan(self):
        for account in self.accounts:
            account.loan_cnt= 2
        print("Loan On")


admin= Admin()

while True:
    print("\nBank Management System")
    print("1-User")
    print("2-Admin")
    print("3-Exit")
    choice = int(input("Please Select User Type: "))

    if choice == 1:
        user_choice = None
        while user_choice != 7:
            print("\n---------------------Menu-------------------")
            print("1-Create Account")
            print("2-Deposit")
            print("3-Withdraw")
            print("4-Check Balance")
            print("5-Transaction History")
            print("6-Transfer Money")
            print("7-Exit")
            user_choice = int(input("Select option: "))

            if user_choice == 1:
                print("\n---------------Please fill the form-------------------")
                name = input("\tName: ")
                email = input("Email: ")
                address = input("Address: ")
                accountNumber = input("Number: ")
                password = input("Password: ")
                account_type = input("Account Type (savings or current): ")
                admin.create_account(name, email, address, accountNumber, password, account_type)
                currentUser = admin.accounts[accountNumber]  
              
            elif user_choice == 2:
                accountNo = input("-----Enter your account number------------- ")
                account_av = admin.accounts.get(accountNo)
                if account_av:
                    amount = float(input("--------Enter deposit amount------ "))
                    account_av.deposit(amount)
                else:
                    print("Account not found")
            elif user_choice== 3:
                accountNo=input("---------Enter your account number-------------- ")
                account_av = admin.accounts.get(accountNo)
                if account_av:
                    amount = float(input("-----------------Enter withdraw amount----------------- "))
                    account_av.withdraw(amount)
                else:
                    print("Account not found")
            elif user_choice == 4:
                accountNo = input("------------Enter your account number----------------")
                account_av = admin.accounts.get(accountNo)
                if account_av:
                   account_av.check_available_balance()  
                else:
                    print("Account not found")
            elif user_choice== 5:
                accountNo=input("---------Enter your account number-------------- ")
                account_av = admin.accounts.get(accountNo)
                if account_av:
                   account_av.check_transaction_history()
                      
                else:
                    print("No Account")
            elif user_choice== 6:
                account1_number= input("---------------Enter your account number-------------")
                account2_number= input("---------Enter target account number-------------")
                amount= float(input("------------Enter transfer amount-------------"))
                account1 = admin.accounts.get(account1_number)
                account2 = admin.accounts.get(account2_number)
                if account1 and account2:
                    account1.transfer(account2, amount)
                else:
                     print("Account not found")
            elif user_choice== 7:
                print("Thank you")
            else:
                print("Invalid option")
    elif choice== 2:
        print("\n----------------------Admin Menu---------------------")
        admin_choice= None
        while admin_choice!= 8:
            print("1-Create Account")
            print("2-Delete Account")
            print("3-See All User Accounts")
            print("4-Total Available Balance")
            print("5-Total Loan Amount")
            print("6-Turn On Loan")
            print("7-Turn Off Loan")
            print("8-Exit")
            admin_choice= int(input("-----------------Select an option---------- "))
            
            if admin_choice== 1:
                print("\n---------------Please fill the form-------------------")
                name = input("\tName: ")
                email = input("Email: ")
                address = input("Address: ")
                accountNumber = input("Number: ")
                password = input("Password: ")
                account_type = input("Account Type (savings or current): ")
                admin.create_account(name, email, address, accountNumber, password, account_type)
                currentUser = admin.accounts[accountNumber] 
            elif admin_choice== 2:
                accountNo=input("-------------Enter account number for delete------------")
                admin.delete_account(accountNo)
            elif admin_choice== 3:
                admin.see_accounts()
            elif admin_choice== 4:
                admin.total_available_balance()
            elif admin_choice== 5:
                admin.total_loans()
            elif admin_choice== 6:
                admin.turnONloan()
            elif admin_choice== 7:
                admin.turnOFFloan()
            elif admin_choice== 8:
                break
            else:
                print("Invalid option")
    elif choice== 3:
        print("Thank you")
        break
    else:
        print("Invalid option")
