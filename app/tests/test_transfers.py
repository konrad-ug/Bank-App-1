import unittest
from ..KontoOsobiste import KontoOsobiste
from parameterized import parameterized

class TestTransfer(unittest.TestCase):
    personal_data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "79103075873"
    }

    @parameterized.expand([
        (100, 100),
        (-100, 0),
    ])
    def test_incomming_transfer(self, transfer_amount, expected_balance):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.zaksięguj_przelew_przychodzący(transfer_amount)
        self.assertEqual(pierwsze_konto.saldo, expected_balance, "Saldo nie jest poprawne")
    
    def test_outgoing_transfer_amount_greater_than_saldo(self):
        pierwsze_konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 50
        pierwsze_konto.przelew_wychodzący(100)
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest poprawne")

    def test_outgoing_transfer_with_promo_code(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"], "PROM_123")
        konto.przelew_wychodzący(20)
        self.assertEqual(konto.saldo, 50 - 20, "Saldo nie jest poprawne!")

    def test_series_of_transfers(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.zaksięguj_przelew_przychodzący(100)
        konto.zaksięguj_przelew_przychodzący(120)
        konto.przelew_wychodzący(50)
        self.assertEqual(konto.saldo, 100 + 120 - 50, "Saldo nie jest porawne")

    def test_express_personal_account(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.saldo = 100
        konto.przelew_wychodzący_ekspresowy(50)
        self.assertEqual(konto.saldo, 100 - 50 - 1, "Saldo nie jest poprawne!")