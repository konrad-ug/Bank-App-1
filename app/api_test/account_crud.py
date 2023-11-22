import unittest
import requests


class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/api/accounts"

    def test_1_create_account(self):
        response = requests.post(self.url, json={"imie": "Jan", "nazwisko": "Kowalski", "pesel": "9103075873"})
        self.assertEqual(response.status_code, 201)

    def test_2_get_account_by_pesel(self):
        response = requests.get(self.url + "/9103075873")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"imie": "Jan", "nazwisko": "Kowalski", "pesel": "9103075873", "saldo": 0 })
    
    def test_3_get_account_non_exist_pesel(self):
        response = requests.get(self.url + "/6969696969")
        self.assertEqual(response.status_code, 404)