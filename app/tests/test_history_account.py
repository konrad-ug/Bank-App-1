import unittest

from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe

class TestHitory(unittest.TestCase):
    personal_data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "79103075873"
    }

    company_data = {
        "name": "nazwaFirmy",
        "nip": "1234567890"
    }

    def test_history_new_account(self):
        new_account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        self.assertEqual(new_account.history, [], "Historia nie jest pusta")

    def test_history_incoming_transfer(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [1000, -200, -1]
        account.zaksięguj_przelew_przychodzący(100)
        self.assertEqual(account.history, [10, -200, -1, 100], "Historia nie jest prawidłowa")

    def test_history_outgoing_transfer(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [1000, -200, -1]
        account.przelew_wychodzący(100)
        self.assertEqual(account.history, [10, -200, -1, -100], "Historia nie jest prawidłowa")

    def test_history_outgoing_express_personal(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [1000, -200, -1]
        account.przelew_wychodzący_ekspresowy(100)
        self.assertEqual(account.history, [10, -200, -1, -100, -1], "Historia nie jest prawidłowa")

    def test_history_outgoing_express_company(self):
        account = KontoFirmowe(self.company_data["name"], self.personal_data["nip"])
        account.history = [1000, -200, 100]
        account.przelew_wychodzący_ekspresowy(100)
        self.assertEqual(account.history, [10, -200, -1, -100, -5], "Historia nie jest prawidłowa")

    def test_history_series_of_transfers(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [1000, -200, -1]
        account.przelew_wychodzący_ekspresowy(100)
        account.zaksięguj_przelew_przychodzący(500)
        account.przelew_wychodzący(50)
        self.assertEqual(account.history, [10, -200, -1, -100, -1, 500, -50], "Historia nie jest prawidłowa")