import unittest
from BankProject.account import Account
from BankProject.account import AmountError

class TestAccount(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        self.account = Account()
    
    def tearDown(self):
        print('Tearing down')

    def test_account_deposit(self):
        self.assertEqual(self.account.deposit('checkings', 100 , '10007'), 1927.0)

    def test_amount_error_deposit(self):
        with self.assertRaises(AmountError):
            self.account.deposit('checkings', -100, '10007')
    
        with self.assertRaises(TypeError):
            self.account.deposit('checkings', 'Hello', '10007')

    def test_account_withdraw(self):
        self.assertEqual(self.account.withdraw('checkings', 100, '10003'), 1700.0 )