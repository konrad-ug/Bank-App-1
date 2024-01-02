import unittest
import requests

class TestSaveLoad(unittest.TestCase):
    url = "http://localhost:5000/api/accounts"
    dane = { "imie": "Jan", "nazwisko": "Kowalski", "pesel": "79103075873"}

    @classmethod
    def setUpClass(cls):
        requests.post(cls.url, json=cls.dane)

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.url}/{cls.dane['pesel']}")

    def test_save_load_account(self):
        response = requests.patch(f"{self.url}/save")
        self.assertEqual(response.status_code, 200)
        
        delete_response = requests.delete(f"{self.url}/{self.dane['pesel']}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(requests.get(f"{self.url}/count").json()["liczba_kont"], 0)

        load_response = requests.patch(f"{self.url}/load")
        self.assertEqual(load_response.status_code, 200)

        get_response = requests.get(f"{self.url}/{self.dane['pesel']}")
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.json(), {'imie': self.dane['imie'], 'nazwisko': self.dane['nazwisko'], 'pesel': self.dane['pesel'], 'saldo': 0})