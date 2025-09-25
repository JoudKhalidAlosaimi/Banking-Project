import csv
from BankProject.bank_system import TestNotString

class Customer:
    def __init__(self):
        pass

    def login(self, first_name, password, account_id):
        self.found = False

        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)

            for row in reader:
                # raise the error here to test it
                    if not first_name.isalpha():
                        raise TestNotString
                    
                    if first_name == row['frst_name'] and password == row['password'] and account_id == row['account_id']:
                        self.found = True

                        return f'Login successful, Welcome {first_name}'
                        # print(f'Login successful , Welcome {first_name}. ')

            if self.found == False:
                print('The password or first name is incorrect , please try again: ')
                    
            # print(all_values)