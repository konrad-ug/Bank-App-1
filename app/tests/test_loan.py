import unittest

from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste

class TestLoan(unittest.TestCase):
    personal_data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "79103075873"
    }
    def test_loan_no_history(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        loan_ability = account.zaciagnij_kredyt(100)
        self.assertFalse(loan_ability)
        self.assertEqual(account.saldo, 0, "Saldo powinno wynosić 0")
    
    def test_loan_3_incoming_transfers(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [-230, 10, 410, 20]
        loan_ability = account.zaciagnij_kredyt(100)
        self.assertTrue(loan_ability)
        self.assertEqual(account.saldo, 100, "Saldo powinno zostać powiększone")
    
    def test_loan_not_incoming_transfers(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [-10, -230, -1, -50]
        account.saldo = 0
        loan_ability = account.zaciagnij_kredyt(100)
        self.assertFalse(loan_ability)
        self.assertEqual(account.saldo, 0, "Saldo nie powinno zostać powiększone")       
        
    def test_loan_5_gt_loan(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [-1, -1, -1, 100, 200]
        account.saldo = 0
        loan_ability = account.zaciagnij_kredyt(100)
        self.assertTrue(loan_ability)
        self.assertEqual(account.saldo, 100, "Saldo powinno zostać powiększone")
