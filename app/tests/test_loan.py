import unittest
from parameterized import parameterized

from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste

class TestLoan(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "79103075873"

    def setUp(self):
        self.konto = KontoOsobiste(self.name, self.surname, self.pesel)

    @parameterized.expand([
        ([], 100, False, 0),
        ([-230, 10, 410, 20], 100, True, 100),
        ([-10, -230, -1, -50], 100, False, 0),
        ([-1, -1, -1, 100, 200], 100, True, 100) 
    ])

    def test_loan(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.history = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)
