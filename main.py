
from BankProject.bank_system import Bank
from BankProject.bank_system import TestNotString
from BankProject.customer import Customer 
from BankProject.account import Account

if __name__ == '__main__':
    start = input('1- New here? 2-Already have an account 3-exit: ')
    if start == '1':
        while True:
            try:
                first_name = input('Enter your first name: ')
                if not first_name.isalpha():
                    raise TestNotString
                last_name = input('Enter your last name: ')
                if not last_name.isalpha():
                    raise TestNotString
            
            except TestNotString:
                print('You have to enter a valid string name')
        
            else:
                password = input('Enter your password: ')
                checking_balance = input('Enter your checking balance: ')
                savings_balance = input('Enter your savings balance: ')
                bank = Bank()
                bank.add_customer(first_name, last_name, password, checking_balance, savings_balance)
                print('Your account has been created! ')
                break
    if start == '2':
        while True:
            user_login = Customer()
            try:
                user_fname = input('Enter your first name: ')
                if not user_fname.isalpha():
                    raise TestNotString
            except TestNotString:
                print('Invalid name, please make sure to enter letters')
            else:
                user_password = input('Enter your password: ')
                user_account_id = input('Enter your accounit id: ')
                if user_login.login(user_fname , user_password, user_account_id):
                    print(f'Welcome {user_fname} , choose what you want to do')
                    user_account_choices = input('1- Deposit 2- Withdraw 3- Transfer: 4-log out:  ')
                    if user_account_choices == '1':
                        account = Account()
                        deposit_account = input('Where do you want to deposit: checkings/savings: ')
                        deposit_amount = float(input('Enter the amount you want to deposit: '))
                        account.deposit(deposit_account, deposit_amount , user_account_id)
                    elif user_account_choices == '4':
                        break
                    # for now
                    break



