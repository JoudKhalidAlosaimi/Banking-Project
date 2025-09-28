import csv
from BankProject.bank_system import AmountError
import datetime as dt
# import time as tm
import random

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
                            row['overdraft_count'] = 0

                        row['balance_checking'] = new_balance        
                
                    elif amount >= 0 and account == 'savings':
                        new_balance = savings + amount
                        row['balance_savings'] = new_balance
                
                    else:
                        raise AmountError
            
        with open('bank.csv','w', newline = '') as f:
            header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings','overdraft_count','account_status']
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
                            row['overdraft_count'] = self.overdraft_count
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
                header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings','overdraft_count','account_status']
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
                            new_checkings = row['balance_checking']
                            new_savings = row['balance_savings']
                            dt.datetime.now()
                            print(f'the new balance of checkings is: {row['balance_checking']}, The new balance of savings is {row['balance_savings']}')

                        elif amount > 0 and savings >= amount and sender_account == 'savings' and receiver_account == 'checkings' and receiver_id == account_id:

                            row['balance_savings'] = savings - amount
                            row['balance_checking'] = checkings + amount
                            new_checkings = row['balance_checking']
                            new_savings = row['balance_savings']
                            dt.datetime.now()
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
                                    dt.datetime.now()
                                    new_checkings = row['balance_checking']
                                    new_savings = row['balance_savings']
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
                                    dt.datetime.now()
                                    new_checkings = row['balance_checking']
                                    new_savings = row['balance_savings']
                                    break

        with open('bank.csv','w', newline = '') as f:
            header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings','overdraft_count','account_status']
            writer = csv.DictWriter(f, fieldnames=header_names)
            writer.writeheader()
            writer.writerows(rows) #stackoverflow

        
        # the bonus
        date = dt.datetime.now()
        transaction_data = [date,sender_account,receiver_account,amount,account_id,receiver_id,new_checkings, new_savings]
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

                    print(f' On {row['date']} , you sent from {row['sender_account']} to {row['receiver_account']}. your new balance for checkings is: {row['sender_new_checking_balance']} your new balance for savings is: {row['sender_new_savings_balance']}')


    def statement(self,account_id):
        
        with open('bank.csv', 'r', newline = '') as f:
            reader = csv.DictReader(f)
            rows = list(reader)


            for row in rows:
                if row['account_id'] == account_id:
                    txt_file = f'{account_id}_statement.txt'
                    new_txt_data = row['balance_checking'] , row['balance_savings'], row['overdraft_count'] ,row['account_status']
                    
                    

                    with open(txt_file , 'a' , newline = '') as f:
                        writer = csv.writer(f)
                        writer.writerow(new_txt_data)

                        print(f'Your checkings current balance is: {row["balance_checking"]}\nYour savings current balance is: {row["balance_savings"]}\nYour overdraft count is: {row["overdraft_count"]}\nYour account status is: {row["account_status"]}')


    def winner(self):
        winner_dict = {}
        with open('bank.csv' , 'r', newline = '') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

            for row in rows:
                checkings = float(row['balance_checking'])
                savings = float(row['balance_savings'])
                user_balances = checkings + savings
                winner_dict[row['account_id']]= user_balances

        sorted_winners = sorted(winner_dict.items(), key= lambda item: item[1], reverse=True) #stackOverflow

        top_three_winners = sorted_winners[:3] #stackOverflow

        winner = random.choice(top_three_winners)
        winner_id = winner[0]
        for row in rows:
            if row['account_id'] == winner_id:
                final_winner_before_balance = row['balance_checking']
                winner_balance = float(row['balance_checking']) + 100
                row['balance_checking'] = winner_balance
                final_winner = row['account_id']
                final_winner_after_balance = row['balance_checking']
                break
                    
                


        print('the 3 top qualifiers were:')
        for account_id , balance in top_three_winners: #stackOverflow
            print(f'Account : {account_id} , Balance: {balance}')

        print(f'the winner is {final_winner}')
        print(f'The winners final checking balance before was {final_winner_before_balance} and now {final_winner_after_balance}')
            


        with open('bank.csv','w', newline = '') as f:
                header_names = ['account_id', 'frst_name','last_name','password','balance_checking','balance_savings','overdraft_count','account_status']
                writer = csv.DictWriter(f, fieldnames=header_names)
                writer.writeheader()
                writer.writerows(rows) #stackoverflow
