import unittest
from BankProject.customer import Customer
from BankProject.bank_system import TestNotString
from BankProject.bank_system import Bank



class TestCustomer(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        account = Bank()
        account.add_customer('joud', 'Alosaimi', 'Jaay10982', 10000, 100 )
        self.customer_login = Customer()
        # self.customer_login.login('joud' , 'joud2018')
        
    
    def tearDown(self):
        print('Tearing down')
        with open('bank.csv' , 'r', newline = '') as f:
            lines = f.readlines()
        lines = lines[:-1]
        
        with open('bank.csv' , 'w', newline= '') as f:
            f.writelines(lines)


    def test_customer_login_success(self):
        self.assertEqual(self.customer_login.login('joud' , 'Jaay10982', '10010'), 'Login successful, Welcome joud')

    def test_customer_raise_error(self):
        with self.assertRaises(TestNotString):
            # self.customer = Customer()
            self.customer_login.login('1000','joud2018', '10007')