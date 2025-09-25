import unittest
import csv
from BankProject.bank_system import Bank
from BankProject.bank_system import TestNotString

class TestBankSystem(unittest.TestCase):
    
    def setUp(self):
        print('Setting up')
        self.bank = Bank()
        self.bank.add_customer('joud', 'Alosaimi', '1234', 10000, 100 )

    def tearDown(self):
        print('Terring down')

    def test_add_valid_customer(self):
        with open('bank.csv', 'r', newline='') as f:
            reader = csv.DictReader(f) # CSV documentation
            # stackOverFlow
            all_values = []
            for row in reader:
                for value in row.values():
                    all_values.append(value)
            self.assertIn('joud', all_values)
            self.assertIn('100', all_values)

            # for row in reader:
            #     print(row['frst_name'])
            #     self.assertIn('joud' , row['frst_name'])

    def test_add_invalid_cutomer(self):
        with self.assertRaises(TestNotString):
            # self.new_bank = Bank()
            self.bank.add_customer('1212' , 'Alosaimi', 1234,10000,1000)

    def test_add_invalid_balance(self):
        with self.assertRaises(ValueError):
            self.bank.add_customer('Jay', 'James', 'jay1010@!!', 100, 'hello')

        with self.assertRaises(TypeError):
            self.bank.add_customer('Reem','Ahmed','10Re@!', -100, -200)