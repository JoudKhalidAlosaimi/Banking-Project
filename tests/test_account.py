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
        self.assertEqual(self.account.deposit('checkings', 100 , '10003'), 4500.0)

    def test_amount_error_deposit(self):
        with self.assertRaises(AmountError):
            self.account.deposit('checkings', -100, '10007')
    
        with self.assertRaises(TypeError):
            self.account.deposit('checkings', 'Hello', '10007')

    def test_account_withdraw(self):
        self.assertEqual(self.account.withdraw('checkings', 100, '10003'), 4400.0 )

    def test_account_transfer(self):
        self.assertEqual(self.account.transfer( 'checkings', 'savings', 100,'10006','10006'), (('55.0', '960.0'), ('55.0', '960.0')))

        self.assertEqual(self.account.transfer( 'checkings', 'another account', 50,'10001','10004'), (('5.0', '10000'), ('2450.0', '20000')))