# import unittest
# from parameterized import parameterized

# from ..Konto import Konto
# from ..KontoOsobiste import KontoOsobiste
# from ..RejestrKont import RejestrKont

# class TestRejestr(unittest.TestCase):

#     imie = "darek"
#     nazwisko = "januszewski"
#     pesel = "79103075873"

#     @classmethod
#     def tearDownClass(cls):
#         RejestrKont.lista = []

#     @classmethod
#     def setUpClass(cls):
#         konto = KontoOsobiste(cls.imie, cls.nazwisko, cls.pesel)
#         RejestrKont.dodaj_konto(konto)

#     def test_1_dodawanie_pierwszego_konta(self):
#         konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
#         konto1 = KontoOsobiste(self.imie, "inny", self.pesel)
#         RejestrKont.dodaj_konto(konto)
#         RejestrKont.dodaj_konto(konto1)
#         self.assertEqual(RejestrKont.ile_kont(), 3)

#     def test_2_znajdź_konto(self):
