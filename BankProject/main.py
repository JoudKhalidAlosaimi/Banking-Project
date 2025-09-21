
from bank_system import Bank

if __name__ == '__main__':
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    password = input('Enter your password: ')
    checking_balance = input('Enter your checking balance: ')
    savings_balance = input('Enter your savings balance: ')
    bank = Bank()
    bank.add_customer(first_name, last_name, password, checking_balance, savings_balance)