import unittest

from parameterized import parameterized
from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "79103075873"
    promo_code = "PROM_XYZ"

    def test_create_account(self):
        konto = Konto()
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(konto.express_transfer_fee, 0, "Opłata za przelew ekspresowy nie jest zerowa!")

    def test_create_personal_account(self):
        pierwsze_konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")

    @parameterized.expand([
        (imie, nazwisko, "1234567890", "Niepoprawny pesel!", "Za krótki pesel został przyjety za prawidłowy!"),
        (imie, nazwisko, "123456789000", "Niepoprawny pesel!", "Za długi pesel został przyjety za prawidłowy!"),
        (imie, nazwisko, "123456789aa", "Niepoprawny pesel!", "Pesel, który nie składa się z samych cyfr został przyjety za prawidłowy!"),
    ])
    def test_pesel_validation(self, imie, nazwisko, pesel, expected_pesel, pesel_msg):
        konto = KontoOsobiste(imie, nazwisko, pesel)
        self.assertEqual(konto.pesel, expected_pesel, pesel_msg)

    @parameterized.expand([
        (imie, nazwisko, pesel, "PROM_", 0, "Saldo nie jest zerowe"),
        (imie, nazwisko, pesel, "prom_123", 0, "Saldo nie jest zerowe"),
        (imie, nazwisko, pesel, "PROM_123sd", 0, "Saldo nie jest zerowe"),
        (imie, nazwisko, pesel, "PROM_123", 50, "Promocja nie została naliczona"),
    ])
    def test_promo_validation(self, imie, nazwisko, pesel, promo_code, expected_saldo, saldo_msg):
        konto = KontoOsobiste(imie, nazwisko, pesel, promo_code)
        self.assertEqual(konto.saldo, expected_saldo, saldo_msg)

    @parameterized.expand([
        (imie, nazwisko, "59041613146", "PROM_123", 0, "Promocja została naliczona, pomimo złego roku urodzenia!"),
        (imie, nazwisko, "61011256976", "PROM_123", 50, "Promocja nie została naliczona, pomimo dobrego roku urodzenia i kodu promocji!"),
        (imie, nazwisko, "01211451663", "PROM_123", 50, "Promocja nie została naliczona, pomimo dobrego roku urodzenia i kodu promocji!"),
        (imie, nazwisko, "01211451663", "PROM_123sdf", 0, "Promocja została naliczona, pomimo złego kodu promocyjnego!"),
    ])
    def test_promo_year_validation(self, imie, nazwisko, pesel, promo_code, expected_saldo, saldo_msg):
        konto = KontoOsobiste(imie, nazwisko, pesel, promo_code)
        self.assertEqual(konto.saldo, expected_saldo, saldo_msg)
