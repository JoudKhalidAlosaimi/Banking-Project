
from bank_system import Bank
from bank_system import TestNotString

if __name__ == '__main__':
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