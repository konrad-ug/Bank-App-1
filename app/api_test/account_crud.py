import unittest
import requests

class TestAccountCrud(unittest.TestCase):
    imie = "darek"
    nazwisko = "januszewski"
    pesel = "79103075873"

    def setUp(self):
        self.url = "http://localhost:5000/api/accounts"

    def test_1_create_account(self):
        response = requests.post(self.url, json={"imie": self.imie, "nazwisko": self.nazwisko, "pesel": self.pesel, "saldo": 0 })
        self.assertEqual(response.status_code, 201)

    def test_2_get_account_by_pesel(self):
        response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"imie": self.imie, "nazwisko": self.nazwisko, "pesel": self.pesel, "saldo": 0 })
    
    def test_3_get_account_non_exist_pesel(self):
        response = requests.get(self.url + "/6969696969")
        self.assertEqual(response.status_code, 404)

    def test_4_update_account(self):
        nowe_imie = "nowe_imie"
        nowe_nazwisko = "nowe_nazwisko"
        nowe_saldo = 100

        response = requests.patch(
            self.url + f"/{self.pesel}",
            json={"imie": nowe_imie, "nazwisko": nowe_nazwisko, "saldo": nowe_saldo},
        )

        self.assertEqual(response.status_code, 200)
        updated_account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(updated_account_response.json(), {"imie": nowe_imie, "nazwisko": nowe_nazwisko, "pesel": self.pesel, "saldo": nowe_saldo})

    def test_5_delete_account(self):
        response = requests.delete(self.url + f"/{self.pesel}")
        self.assertEqual(response.status_code, 200)
    
        deleted_account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(deleted_account_response.status_code, 404)

    def test_6_create_second_account_with_the_same_pesel(self):
        requests.post(self.url, json={"imie": self.imie, "nazwisko": self.nazwisko, "pesel": self.pesel, "saldo": 0 })
        response = requests.post(self.url, json={"imie": self.imie, "nazwisko": self.nazwisko, "pesel": self.pesel, "saldo": 0 })
        self.assertEqual(response.status_code, 409)
