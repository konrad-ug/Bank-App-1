import unittest
import requests

class TestTransfer(unittest.TestCase):
    imie = "darek"
    nazwisko = "januszewski"
    pesel = "79103075873"
    url = "http://localhost:5000/api/accounts"

    inny_pesel = "89102846482"

    def setUp(self):
        requests.post(self.url, json={"imie": self.imie, "nazwisko": self.nazwisko, "pesel": self.pesel } )

    def tearDown(self):
        requests.delete(self.url + "/" + self.pesel)

    def test_1_successful_incoming_transfer(self):
        transfer_response = requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 500, "type": "incoming"})
        self.assertEqual(transfer_response.status_code, 200)
        account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(account_response.status_code, 200)
        self.assertEqual(account_response.json()["saldo"], 500)

    def test_2_incoming_transfer_non_existing_account(self):
        transfer_response = requests.post(self.url + f"/{self.inny_pesel}/transfer", json={"amount": 500, "type": "incoming"})
        self.assertEqual(transfer_response.status_code, 404)
        account_response = requests.get(self.url + f"/{self.inny_pesel}")
        self.assertEqual(account_response.status_code, 404)

    def test_3_successful_outgoing_transfer(self):
        requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 500, "type": "incoming"})
        transfer_response = requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 20, "type": "outgoing"})
        self.assertEqual(transfer_response.status_code, 200)

        account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(account_response.status_code, 200)
        self.assertEqual(account_response.json()["saldo"], 480)

    def test_4_outgoing_transfer_luck_of_funds(self):
        transfer_response = requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 20, "type": "outgoing"})
        self.assertEqual(transfer_response.status_code, 422)

        account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(account_response.json()["saldo"], 0)
