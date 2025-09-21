import csv
import uuid

class Bank:
    def __init__(self):
        pass

    def add_customer(self, first_name , last_name , password, checking_balance , savings_balance):
        user_id = uuid.uuid4() #GeeksforGeeks
        data = [user_id, first_name , last_name , password, checking_balance , savings_balance]
        with open('bank.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        print('Your account has been created! ')

