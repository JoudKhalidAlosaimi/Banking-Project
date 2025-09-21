import csv
import uuid

class TestNotString(Exception):
    pass

class Bank:
    def __init__(self):
        pass

    def add_customer(self, first_name , last_name , password, checking_balance , savings_balance):
        user_id = uuid.uuid4() #GeeksforGeeks
        if not first_name.isalpha() or not last_name.isalpha():
            raise TestNotString
        data = [user_id, first_name , last_name , password, checking_balance , savings_balance]
        with open('bank.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
