import unittest
import csv 
from BankProject.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        print('Setting up')
        self.customer_login = Customer()
        # self.customer_login.login('joud' , 'joud2018')
    
    def tearDown(self):
        print('Tearing down')

    def test_customer_login_success(self):
        self.assertEqual(self.customer_login.login('joud' , 'joud2018'), 'Login successful, Welcome joud')