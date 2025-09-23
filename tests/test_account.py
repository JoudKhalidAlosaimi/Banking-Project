import unittest
from BankProject.account import Account
from BankProject.account import AmountError

class TestAccount(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        self.new_deposit = Account()
    
    def tearDown(self):
        print('Tearing down')

    def test_account_deposit(self):
        self.assertEqual(self.new_deposit.deposit('checkings', 22, '68da891c-f017-4ad6-a711-d28897ee7ae8'), 101176.0)

    def test_amount_error(self):
        with self.assertRaises(AmountError):
            self.new_deposit.deposit('checkings', -100, '68da891c-f017-4ad6-a711-d28897ee7ae8')
    
        with self.assertRaises(TypeError):
            self.new_deposit.deposit('checkings', 'Hello', '68da891c-f017-4ad6-a711-d28897ee7ae8')