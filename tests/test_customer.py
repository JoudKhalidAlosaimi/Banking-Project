import unittest
from BankProject.customer import Customer
from BankProject.bank_system import TestNotString



class TestCustomer(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        self.customer_login = Customer()
        # self.customer_login.login('joud' , 'joud2018')
        
    
    def tearDown(self):
        print('Tearing down')

    def test_customer_login_success(self):
        self.assertEqual(self.customer_login.login('joud' , 'joud2018'), 'Login successful, Welcome joud')

    def test_customer_raise_error(self):
        with self.assertRaises(TestNotString):
            # self.customer = Customer()
            self.customer_login.login('1000','joud2018')