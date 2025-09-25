import csv
from BankProject.bank_system import AmountError

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
        # new_balance = None
        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            

            for row in rows:
                checkings = float(row['balance_checking'])
                savings = float(row['balance_savings'])

                if row['account_id'] == account_id:
                    if amount >= 0 and account == 'checkings':
                        new_balance = checkings - amount
                        if new_balance < 0 and amount < 100:
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
    

    def transfer(self,sender_account,receiver_account,amount,account_id,receiver_id):
        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            

            for row in rows:
                checkings = float(row['balance_checking'])
                savings = float(row['balance_savings'])

                if row['account_id'] == account_id:

                        if amount > 0 and checkings >= amount and sender_account == 'checkings' and receiver_account == 'savings' and receiver_id == account_id:

                            row['balance_checking'] = checkings - amount
                            row['balance_savings'] = savings + amount
                            print(f'the new balance of checkings is: {row['balance_checking']}, The new balance of savings is {row['balance_savings']}')

                        elif amount > 0 and savings >= amount and sender_account == 'savings' and receiver_account == 'checkings' and receiver_id == account_id:

                            row['balance_savings'] = savings - amount
                            row['balance_checking'] = checkings + amount
                            print(f'the new balance of checkings is: {row['balance_checking']}, The new balance of savings is {row['balance_savings']}')


                        elif amount > 0 and savings >= amount and sender_account == 'savings' and receiver_account == 'another account':
                            row['balance_savings'] = savings - amount # sender 

                            # loop to find the receiver
                            for receiver in rows:
                                if receiver['account_id'] == receiver_id:
                                    receiver_checkings = float(receiver['balance_checking'])
                                    receiver['balance_checking'] = receiver_checkings + amount
                                    # print(f'the new balance of checkings receiver: {receiver['balance_checking']}')
                                    print(f'the new balance of your savings: {row["balance_savings"]}')
                                    break
                                # print(f'the new balance of savings sender: {row['balance_savings']}')
                        
                        elif amount > 0 and checkings >= amount and sender_account == 'checkings' and receiver_account == 'another account':
                            row['balance_checking'] = checkings - amount # sender 

                            # loop to find the receiver
                            for receiver in rows:
                                if receiver['account_id'] == receiver_id:
                                    receiver_checkings = float(receiver['balance_checking'])
                                    receiver['balance_checking'] = receiver_checkings + amount
                                    print(f'the new balance of your checkings: {row["balance_checking"]}')
                                    
                                    break

        with open('bank.csv','w', newline = '') as f:
            header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings','account_status']
            writer = csv.DictWriter(f, fieldnames=header_names)
            writer.writeheader()
            writer.writerows(rows) #stackoverflow

        
        # the bonus
        transaction_data = [sender_account,receiver_account,amount,account_id,receiver_id,row['balance_checking'], row['balance_savings']]
        with open('transaction.csv' , 'a' , newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(transaction_data)



            for row in rows:
                if row['account_id'] == account_id:
                    sender_balance =  (row['balance_checking'] , row['balance_savings'])

                if row['account_id'] == receiver_id:
                    receiver_balance = (row['balance_checking'], row['balance_savings'])

            return sender_balance , receiver_balance
        

    def transaction_details(self,sender_id):

        with open('transaction.csv' , 'r' , newline = '') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

            for row in rows:
                if row['account_id'] == sender_id:

                    print(f'you sent from {row['sender_account']} account, to {row['receiver_account']}, your new balance for checkings is: {row['sender_new_checking_balance']} your new balance for savings is: {row['sender_new_savings_balance']}')


            





