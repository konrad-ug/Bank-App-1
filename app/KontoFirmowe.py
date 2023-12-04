from .Konto import Konto
from datetime import datetime
import os
import requests

class KontoFirmowe(Konto):
    express_transfer_fee = 5

    def __init__(self, name, nip):
        self.name = name
        self.saldo = 0
        self.history = []
        
        if len(nip) == 10:
            if self.is_nip_correct(nip):
                self.nip = nip
            else:
                raise Exception("NIP does not exist in gov!")
        else:
            self.nip = "Niepoprawny NIP!"

    def zaciagnij_kredyt(self, kwota):
        if self.saldo >= 2 * kwota and -1775 in self.history:
            self.saldo += kwota
            return True
        return False

    @classmethod
    def is_nip_correct(cls, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-api.mf.gov.pl/')
        date = datetime.now().date()
        nip_path = f"{gov_url}api/search/nip/{nip}/?date={date}"
        print(f"sending requests to {nip_path}")
        response = requests.get(nip_path)
        print(f"Response dla nipu: {response.status_code}, {response.json()}")
        return response.status_code == 200
