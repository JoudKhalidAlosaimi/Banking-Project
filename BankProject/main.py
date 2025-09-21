
from bank_system import Bank
from bank_system import TestNotString
from customer import Customer 

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
            user_fname = input('Enter your first name: ')
            user_password = input('Enter your password: ')
            user_login.login(user_fname , user_password)
            user_account_choices = input('1- Withdraw 2- Deposit 3- Transfer: ')

