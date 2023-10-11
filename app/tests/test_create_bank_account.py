import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678910"
    promo_code = "PROM_XYZ"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
    
    def test_pesel_with_len_10(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za krótki pesel został przyjety za prawidłowy!")

    def test_pesel_with_len_12(self):
        konto = Konto(self.imie, self.nazwisko, "123456789000")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za długi pesel został przyjety za prawidłowy!")

    def test_pesel_empty(self):
        konto = Konto(self.imie, self.nazwisko, '')
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pusty pesel został przyjęty za prawidłowy")

    def test_promo_wron_len(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_promo_wrong_preffix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "prom_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")
    
    def test_promo_wrong_suffix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_123sd")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe")

    def test_promo_correct(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_123")
        self.assertEqual(konto.saldo, 50, "Promocja nie została naliczona")

    def test_promo_year_59(self):
    def test_promo_year_61(self):
    def test_promo_year_60(self):
    def test_promo_year_2001(self):
    def test_promo_year_2001_wrong_promo_code(self):
    def test_promo_year_correct_promo_code_wrong_pesel(self):



    #tutaj proszę dodawać nowe testy