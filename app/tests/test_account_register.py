import unittest
from parameterized import parameterized
from unittest.mock import patch

from ..Konto import Konto
from ..KontoOsobiste import KontoOsobiste
from ..RejestrKont import RejestrKont

class TestRejestr(unittest.TestCase):

    imie = "darek"
    nazwisko = "januszewski"
    pesel = "79103075873"

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista_kont = []

    @classmethod
    def setUpClass(cls):
        RejestrKont.lista_kont = []

    def test_rejestr(self):
        RejestrKont.lista_kont = []
        nowe_konto1 = KontoOsobiste("imie1", "nazwisko1", "95102866489")
        nowe_konto2 = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(nowe_konto1)
        RejestrKont.dodaj_konto(nowe_konto2)
        self.assertEqual(RejestrKont.ile_kont(), 2)
        self.assertEqual(RejestrKont.znajdź_konto(self.pesel), nowe_konto2)
        self.assertEqual(RejestrKont.znajdź_konto("94101913536"), None)
        RejestrKont.lista_kont = []

    @patch('app.RejestrKont.RejestrKont.collection')
    def test_load_emptying_list(self, mock_collection):
        mock_collection.find.return_value = [
            {"imie": "Jan", "nazwisko": "Kowalski", "pesel": "79103075873", "saldo": 1000, "history": []}
        ]
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        RejestrKont.load()
        self.assertEqual(len(RejestrKont.lista_kont), 1)
        self.assertEqual(RejestrKont.lista_kont[0].imie, 'Jan')
        self.assertEqual(RejestrKont.lista_kont[0].nazwisko, 'Kowalski')
        self.assertEqual(RejestrKont.lista_kont[0].pesel, '79103075873')
        self.assertEqual(RejestrKont.lista_kont[0].saldo, 1000)
        self.assertEqual(RejestrKont.lista_kont[0].history, [])

    
    @patch('app.RejestrKont.RejestrKont.collection')
    def test_load(self, mock_collection):
        mock_collection.find.return_value = [
            {"imie": "Jan", "nazwisko": "Kowalski", "pesel": "79103075873", "saldo": 1000, "history": []}
        ]
        RejestrKont.load()
        self.assertEqual(len(RejestrKont.lista_kont), 1)
        self.assertEqual(RejestrKont.lista_kont[0].imie, 'Jan')
        self.assertEqual(RejestrKont.lista_kont[0].nazwisko, 'Kowalski')
        self.assertEqual(RejestrKont.lista_kont[0].pesel, '79103075873')
        self.assertEqual(RejestrKont.lista_kont[0].saldo, 1000)
        self.assertEqual(RejestrKont.lista_kont[0].history, [])

    
    @patch('app.RejestrKont.RejestrKont.collection')
    def test_save(self, mock_collection):
        konto = KontoOsobiste("Jan", "Kowalski", "79103075873")
        konto.saldo = 1000
        konto.history = [300, -200, 500]
        RejestrKont.dodaj_konto(konto)
        RejestrKont.save()
        mock_collection.delete_many.assert_called_once_with({})
        mock_collection.insert_one.assert_called_once_with({"imie": "Jan", "nazwisko": "Kowalski", "pesel": "79103075873", "saldo": 1000, "history": [300, -200, 500]})
    