import csv
import re #GeeksforGeeks , provides support for regular expressions 

class TestNotString(Exception):
    pass

class AmountError(Exception):
    pass

class PasswordError(Exception):
    pass

class Bank:
    def __init__(self):
        pass


    def generate_customer_id(self):
        self.customers = []
        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            for row in rows:
                self.customers.append(row['account_id'])
            # Credits to Conor and Rana for helping in this part
            if not self.customers:
                return "10001"
            max_id = max(int(row['account_id']) for customer in self.customers)
            return str(max_id + 1) 

    def add_customer(self, first_name , last_name , password, checking_balance , savings_balance):
        # user_id = uuid.uuid4() #GeeksforGeeks
        account_status = 'active'
        account_id = self.generate_customer_id()
        # raise the error here to test it in unit test
        if not first_name.isalpha() or not last_name.isalpha():
            raise TestNotString
        
        #new
        if not float(checking_balance) or not float(savings_balance):
            raise ValueError
        
        if checking_balance < 0 or savings_balance < 0:
            raise TypeError
        
        
        if len(password) < 8 or not re.search('[a-z]' ,password) or not re.search('[A-Z]' ,password) or not re.search('[0-9]' , password):
                # print('Password is too weak , make sure you add 8 characters including Capital letters , small letters, and numbers')
                raise PasswordError
                
        

        data = [account_id, first_name , last_name , password, checking_balance , savings_balance, account_status]
        with open('bank.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
