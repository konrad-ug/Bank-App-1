import unittest
import requests


class TestPerformance(unittest.TestCase):
    imie = "darek"
    nazwisko = "januszewski"
    pesel = "79103075873"
    url = "http://localhost:5000/api/accounts"


    def test_create_and_delete_accounts_performance(self):
        for _ in range(100):
            create_response = requests.post(
                self.url,
                json={"imie": self.imie, "nazwisko": self.nazwisko, "pesel": self.pesel},
                timeout=2
            )

            self.assertEqual(create_response.status_code, 201)
            self.assertLess(create_response.elapsed.total_seconds(), 2)

            delete_url = f"{self.url}/{self.pesel}"
            delete_response = requests.delete(delete_url, timeout=2)

            self.assertEqual(delete_response.status_code, 200)
            self.assertLess(delete_response.elapsed.total_seconds(), 2)
