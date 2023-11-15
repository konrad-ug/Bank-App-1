import unittest
from parameterized import parameterized

from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..RejestrKont import RejestrKont

class TestRejestr(unittest.TestCase):

    imie = "darek"
    nazwisko = "januszewski"
    pesel = "79103075873"
    konto = KontoOsobiste(imie, nazwisko, pesel)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista_kont = []

    @classmethod
    def setUpClass(cls):
        RejestrKont.dodaj_konto(cls.konto)

    def test_rejestr(self):
        nowe_konto = KontoOsobiste("imie1", "nazwisko1", "95102866489")
        RejestrKont.dodaj_konto(nowe_konto)
        self.assertEqual(RejestrKont.ile_kont(), 2)
        self.assertEqual(RejestrKont.znajdź_konto(self.pesel), self.konto)
        self.assertEqual(RejestrKont.znajdź_konto("94101913536"), None)

