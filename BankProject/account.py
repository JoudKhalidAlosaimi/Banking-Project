import csv

class AmountError(Exception):
    pass

class Account:
    def __init__(self):
        pass

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
                        row['balance_checking'] = new_balance
                    
                
                    elif amount >= 0 and account == 'savings':
                        new_balance = savings + amount
                        row['balance_savings'] = new_balance
                
                    else:
                        raise AmountError
            
        with open('bank.csv','w', newline = '') as f:
            header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings']
            writer = csv.DictWriter(f, fieldnames=header_names)
            writer.writeheader()
            writer.writerows(rows) #stackoverflow

        print(f'The new balance of {account} is {new_balance}')
        return new_balance
