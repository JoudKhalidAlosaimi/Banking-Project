import csv

class Customer:
    def __init__(self):
        pass

    def login(self , password):
        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            password_values = []
            for row in reader:
                password_values.append(row['password'])
            # print(password_values)

            for value in password_values:
                if password == value:
                    print('The password is correct')
                    break
            else:
                print('The password is not correct')