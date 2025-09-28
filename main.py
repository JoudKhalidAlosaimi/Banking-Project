from BankProject.bank_system import Bank
from BankProject.bank_system import TestNotString
from BankProject.customer import Customer 
from BankProject.account import Account
from BankProject.bank_system import AmountError
from BankProject.bank_system import PasswordError
import re #GeeksforGeeks


if __name__ == '__main__':
        start = input('1- New here?  2-Already have an account 3-Todays winner 4-exit: ')
        if start == '1':
            while True:
                    try:
                        first_name = input('Enter your first name: ')
                        if not first_name.isalpha():
                            raise TestNotString


                        last_name = input('Enter your last name: ')
                        if not last_name.isalpha():
                            raise TestNotString

                        checking_balance = float(input('Enter your checking balance: '))
                        if not float(checking_balance):
                            raise ValueError
                        elif checking_balance < 0:
                            raise TypeError

                        savings_balance = float(input('Enter your savings balance: '))
                        if not float(savings_balance):
                            raise ValueError
                        elif savings_balance < 0:
                            raise TypeError
                        
                        password = input('Enter your password: ')
                        #GeeksforGeeks
                        if len(password) < 8 or not re.search('[a-z]' ,password) or not re.search('[A-Z]' ,password) or not re.search('[0-9]' , password):
                            raise PasswordError
            
                    except TestNotString:
                        print('You have to enter a valid string name')

                    except ValueError:
                        print('Please enter a valid number')

                    except TypeError:
                        print('Please enter a positive number')
                    
                    except PasswordError:
                        print('Password is too weak , make sure you add 8 characters including Capital letters , small letters, and numbers')
                
                    else:
                        # password = input('Enter your password: ')
                        bank = Bank()
                        bank.add_customer(first_name, last_name, password, checking_balance, savings_balance)
                        print('Your account has been created! ')
                        break

        if start == '2':
            while True:
                user_login = Customer()
                try:
                    user_fname = input('Enter your first name: ')
                    if not user_fname.isalpha():
                        raise TestNotString
                except TestNotString:
                    print('Invalid name, please make sure to enter letters')
                else:
                    user_password = input('Enter your password: ')
                    user_account_id = input('Enter your accounit id: ')
                    if user_login.login(user_fname , user_password, user_account_id):
                        print(f'Welcome {user_fname} , choose what you want to do')
                        account = Account()
                        while True:
                            user_account_choices = input('1- Deposit 2- Withdraw 3- Transfer: 4-Transaction details 5-Statement Report 6-log out:  ')
                            if user_account_choices == '1':
                                # account = Account()
                                deposit_account = input('Where do you want to deposit: checkings/savings: ')
                                while True:
                                    try :
                                        # account = Account()
                                        # deposit_account = input('Where do you want to deposit: checkings/savings: ')
                                        deposit_amount = float(input('Enter the amount you want to deposit: '))
                                        account.deposit(deposit_account, deposit_amount , user_account_id)
                                        break

                                    except AmountError:
                                        print('Please enter a positive number')
                            elif user_account_choices == '2':
                                # account = Account()
                                withdraw_account = input('Where do you want to withdraw from: checkings/savings: ')
                                while True:
                                    try :
                                        withdraw_amount = float(input('Enter the amount you want to withdraw: '))
                                        account.withdraw(withdraw_account, withdraw_amount , user_account_id)
                                        break

                                    except AmountError:
                                        print('the amount must be positive')
                                        
                            elif user_account_choices == '3':
                                transfer_account_from = input('Enter where you want to tranfer from: checkings/savings: ')
                                transfer_account_to = input('Enter where you want to transfer to: checkings/savings/another account: ')
                                # if transfer_account_to == 'another account':
                                receiver_account_id = input('Enter the id of the account you want to transfer to: ')
                                while True:
                                    try :
                                        transfer_amount = float(input('Enter the amount you want to transfer: '))
                                        account.transfer( transfer_account_from, transfer_account_to, transfer_amount,user_account_id,receiver_account_id)
                                        break
                                    except AmountError:
                                        print('Please enter a positive number')
                            elif user_account_choices == '4':
                                account.transaction_details(user_account_id)
                            elif user_account_choices == '5':
                                account.statement(user_account_id)

                            elif user_account_choices == '6':
                                break
        if start == '3':
            winner = Account()
            winner.winner()
            
        if start == '4':
            while True:
                break
            
                        
                        
                        
