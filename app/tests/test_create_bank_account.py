import unittest

# from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "79103075873"
    promo_code = "PROM_XYZ"

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
    
    def test_pesel_with_len_10(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za krótki pesel został przyjety za prawidłowy!")

    def test_pesel_with_len_12(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "123456789000")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za długi pesel został przyjety za prawidłowy!")
    
    def test_pesel_not_number(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "123456789aa")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pesel, który nie składa się z samych cyfr został przyjety za prawidłowy!")

    def test_pesel_wrong_numbers(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "12345678910")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pesel, który nie istnieje został przyjęty za prawidłowy!")

    def test_pesel_empty(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, '')
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pusty pesel został przyjęty za prawidłowy")

    def test_promo_wron_len(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "PROM_")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_promo_wrong_preffix(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "prom_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")
    
    def test_promo_wrong_suffix(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "PROM_123sd")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_promo_correct(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "PROM_123")
        self.assertEqual(konto.saldo, 50, "Promocja nie została naliczona")

    def test_promo_year_59(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "59041613146", "PROM_123")
        self.assertEqual(konto.saldo, 0, "Promocja została naliczona, pomimo złego roku urodzenia!")

    def test_promo_year_61(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "61011256976", "PROM_123")
        self.assertEqual(konto.saldo, 50, "Promocja nie została naliczona, pomimo dobrego roku urodzenia i kodu promocji!")

    def test_promo_year_2001(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "01211451663", "PROM_123")
        self.assertEqual(konto.saldo, 50, "Promocja nie została naliczona, pomimo dobrego roku urodzenia i kodu promocji!")

    def test_promo_year_2001_wrong_promo_code(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "01211451663", "PROM_123sdf")
        self.assertEqual(konto.saldo, 0, "Promocja została naliczona, pomimo złego kodu promocyjnego!")

