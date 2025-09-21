import csv
import uuid

class Bank:
    def __init__(self):
        self.customers = [] 
        self.accounts = []

    def add_customer(self, first_name , last_name , password, checking_balance , savings_balance):
        user_id = uuid.uuid4() #GeeksforGeeks
        data = [user_id, first_name , last_name , password, checking_balance , savings_balance]
        with open('bank.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        print('Your account has been created! ')


if __name__ == '__main__':
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    password = input('Enter your password: ')
    checking_balance = input('Enter your checking balance: ')
    savings_balance = input('Enter your savings balance: ')
    bank = Bank()
    bank.add_customer(first_name, last_name, password, checking_balance, savings_balance)