import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from datetime import datetime
from parameterized import parameterized
from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe
from ..SMTPConnection import SMTPConnection

class TestHistory(unittest.TestCase):
    personal_data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "79103075873"
    }

    company_data = {
        "name": "nazwaFirmy",
        "nip": "1234567890"
    }

    def test_personal_send_mail_with_history(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.saldo = 1000
        konto.przelew_wychodzący(100)
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_konto("d_januszewski@gmail.com", smtp_connection)
        self.assertTrue(status)
        data = datetime.now().date()
        smtp_connection.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {data}",
            f"Twoja historia konta to: {konto.history}",
            "d_januszewski@gmail.com"
            )
        
    def test_personal_send_mail_with_history_failed(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.saldo = 1000
        konto.przelew_wychodzący(100)
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value = False)
        status = konto.wyslij_historie_na_konto("d_januszewski@gmail.com", smtp_connection)
        self.assertFalse(status)
        data = datetime.now().date()
        smtp_connection.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {data}",
            f"Twoja historia konta to: {konto.history}",
            "d_januszewski@gmail.com"
            )
    
    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_correct')
    def test_company_send_mail_with_history(self, mock_is_nip_correct):
        mock_is_nip_correct.return_value = True
        konto = KontoFirmowe(self.company_data["name"], self.company_data["nip"])
        konto.saldo = 1000
        konto.przelew_wychodzący(100)
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_konto("d_januszewski@gmail.com", smtp_connection)
        self.assertTrue(status)
        data = datetime.now().date()
        smtp_connection.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {data}",
            f"Historia konta Twojej firmy to: {konto.history}",
            "d_januszewski@gmail.com"
            )
    
    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_correct')
    def test_company_send_mail_with_history_failed(self, mock_is_nip_correct):
        mock_is_nip_correct.return_value = True
        konto = KontoFirmowe(self.company_data["name"], self.company_data["nip"])
        konto.saldo = 1000
        konto.przelew_wychodzący(100)
        smtp_connection = SMTPConnection()
        smtp_connection.wyslij = MagicMock(return_value = False)
        status = konto.wyslij_historie_na_konto("d_januszewski@gmail.com", smtp_connection)
        self.assertFalse(status)
        data = datetime.now().date()
        smtp_connection.wyslij.assert_called_once_with(
            f"Wyciąg z dnia {data}",
            f"Historia konta Twojej firmy to: {konto.history}",
            "d_januszewski@gmail.com"
            )

    def test_history_new_account(self):
        new_account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        self.assertEqual(new_account.history, [], "Historia nie jest pusta")

    def test_history_incoming_transfer(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [1000]
        account.saldo = 1000
        account.zaksięguj_przelew_przychodzący(100)
        self.assertEqual(account.history, [1000, 100], "Historia nie jest prawidłowa")

    def test_history_outgoing_transfer(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [1000]
        account.saldo = 1000
        account.przelew_wychodzący(100)
        self.assertEqual(account.history, [1000, -100], "Historia nie jest prawidłowa")

    def test_history_outgoing_express_personal(self):
        account = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        account.history = [1000]
        account.saldo = 1000
        account.przelew_wychodzący_ekspresowy(100)
        self.assertEqual(account.history, [1000, -100, -1], "Historia nie jest prawidłowa")

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_correct')
    def test_history_outgoing_express_company(self, mock_is_nip_correct):
        mock_is_nip_correct.return_value = True
        account = KontoFirmowe(self.company_data["name"], self.company_data["nip"])
        account.history = [1000]
        account.saldo = 1000
        account.przelew_wychodzący_ekspresowy(100)
        self.assertEqual(account.history, [1000, -100, -5], "Historia nie jest prawidłowa")
