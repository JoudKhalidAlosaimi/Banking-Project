import unittest
import csv
from BankProject.bank_system import Bank

class TestBankSystem(unittest.TestCase):
    
    def setUp(self):
        self.bank = Bank()
        self.bank.add_customer('joud', 'Alosaimi', '1234', 10000, 100 )

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