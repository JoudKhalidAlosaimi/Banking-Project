import csv

class TestNotString(Exception):
    pass

class AmountError(Exception):
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
        

        data = [account_id, first_name , last_name , password, checking_balance , savings_balance, account_status]
        with open('bank.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
