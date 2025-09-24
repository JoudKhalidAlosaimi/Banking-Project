import csv

class AmountError(Exception):
    pass

class Account:
    def __init__(self):
        self.overdraft_count = 0


    def deposit(self, account, amount , account_id):
        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader) #stackOverflow

            for row in rows:
                checkings = float(row['balance_checking'])
                savings = float(row['balance_savings'])

                if row['account_id'] == account_id:
                    if amount >= 0 and account == 'checkings':
                        new_balance = checkings + amount
                        # row['balance_checking'] = new_balance
                    
                        if new_balance >= 0:
                            # print('your account is now active!')
                            row['account_status'] = 'active'

                        row['balance_checking'] = new_balance        
                
                    elif amount >= 0 and account == 'savings':
                        new_balance = savings + amount
                        row['balance_savings'] = new_balance
                
                    else:
                        raise AmountError
            
        with open('bank.csv','w', newline = '') as f:
            header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings','account_status']
            writer = csv.DictWriter(f, fieldnames=header_names)
            writer.writeheader()
            writer.writerows(rows) #stackoverflow

        print(f'The new balance of {account} is {new_balance}')
        return new_balance
    
    def withdraw(self,account, amount, account_id):
        new_balance = None
        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            

            for row in rows:
                checkings = float(row['balance_checking'])
                savings = float(row['balance_savings'])

                if row['account_id'] == account_id:
                    
                    if amount >= 0 and amount <= 100 and account == 'checkings':
                        new_balance = checkings - amount
                        if new_balance < 0:
                            new_balance -= 35

                        if new_balance < -100:
                            self.overdraft_count += 1
                            print('Withdraw denied, you reached the limit')
                            # print(self.overdraft_count)
            
                            if self.overdraft_count == 2:
                                print('Account deactivaed, pay your overdraft amount and fee to reactivate')
                                row['account_status'] = 'deactivated'

                        else:
                            row['balance_checking'] = new_balance
                            print(f'The new balance of {account} is {new_balance}')
                            # return f' the balance of the {account} is {new_balance}'
                            
                            

                    elif amount >= 0 and amount <= 100 and account == 'savings':
                        new_balance = savings - amount
                        if new_balance < 0:
                            print('sorry withdraw denied , you have reached the limit.')

                        else:
                            row['balance_savings'] = new_balance
                            print(f'The new balance of {account} is {new_balance}')
                            # return f' the balance of the {account} is {new_balance}'
                    
                    

        
        with open('bank.csv','w', newline = '') as f:
            header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings','account_status']
            writer = csv.DictWriter(f, fieldnames=header_names)
            writer.writeheader()
            writer.writerows(rows) #stackoverflow
            

        
        return new_balance
    








