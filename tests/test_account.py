import unittest
from BankProject.account import Account
from BankProject.account import AmountError
from BankProject.bank_system import Bank

class TestAccount(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        account = Bank()
        account.add_customer('joud', 'Alosaimi', 'Jaay10982', 10000, 100 )
        self.account = Account()
    
    def tearDown(self):
        print('Tearing down')
        with open('bank.csv' , 'r', newline = '') as f:
            lines = f.readlines()
        lines = lines[:-1]
        
        with open('bank.csv' , 'w', newline= '') as f:
            f.writelines(lines)



    def test_account_deposit(self):
        self.assertEqual(self.account.deposit('checkings', 1000 , '10010'), 11000)

    def test_amount_error_deposit(self):
        with self.assertRaises(AmountError):
            self.account.deposit('checkings', -100, '10010')
    
        with self.assertRaises(TypeError):
            self.account.deposit('checkings', 'Hello', '10010')

    def test_account_withdraw(self):
        self.assertEqual(self.account.withdraw('checkings', 1000, '10010'), 9000.0)

    def test_account_transfer(self):
        self.assertEqual(self.account.transfer( 'checkings', 'savings', 100,'10010','10010'), ((9900.0, 200.0), (9900.0, 200.0)))

        self.assertEqual(self.account.transfer( 'savings', 'checkings', 50,'10010','10010'), ((9950.0, 150.0), (9950.0, 150.0))) 