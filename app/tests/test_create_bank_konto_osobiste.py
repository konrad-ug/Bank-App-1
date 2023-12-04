import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe
import requests

class TestCreateBankAccount(unittest.TestCase):
    name = "JOG"
    nip = "8461627563"
    wrong_nip = "7461617563"

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_correct')
    def test_create_account_with_correct_nip(self, mock_is_nip_correct):
        mock_is_nip_correct.return_value = True
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Nazwa nie jest poprawne")
        self.assertEqual(pierwsze_konto.nip, self.nip, "NIP nie jest poprawny")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe")


    def test_create_account_with_wrong_length_nip(self):
        konto = KontoFirmowe(self.name, "123456789")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "Nip incorrect")


    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_correct')
    def test_create_account_with_nip_not_in_gov(self, mock_is_nip_correct):
        mock_is_nip_correct.return_value = False
        with self.assertRaises(Exception) as context:
            KontoFirmowe(self.name, "7461617563")
        self.assertIn("NIP does not exist in gov!", str(context.exception))
