import unittest
from parameterized import parameterized

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestLoanCompany(unittest.TestCase):
    name = "Company_name"
    nip = "1234567890"

    def setUp(self):
        self.konto = KontoFirmowe(self.name, self.nip)

    @parameterized.expand([
        ([], 0, 100, False, 0), # brak Zusu, za małe saldo
        ([-1775, 3000], 3000, 100, True, 3100), # wszystko git
        ([3000], 3000, 100, False, 3000), # brak Zusu
        ([-1775], 10, 100, False, 10) # za małe saldo
    ])

    def test_loan_company(self, historia, saldo, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.history = historia
        self.konto.saldo = saldo
        czy_przyznany = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)


