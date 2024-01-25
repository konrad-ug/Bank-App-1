from datetime import datetime
from .SMTPConnection import SMTPConnection
class Konto:
    def __init__(self):
        self.express_transfer_fee = 0
        self.saldo = 0
        self.history = []
        self.email_msg = ""
        
 
    def zaksięguj_przelew_przychodzący(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            self.history.append(kwota)

    def przelew_wychodzący(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota
            self.history.append(-kwota)

    def przelew_wychodzący_ekspresowy(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota
            self.saldo -= self.express_transfer_fee
            self.history.append(-kwota)
            self.history.append(-self.express_transfer_fee)

    def wyslij_historie_na_konto(self, adresat, smtp_conntection):
        tresc = f"{self.email_msg}: {self.history}"
        data = datetime.now().date()
        temat = f"Wyciąg z dnia {data}"
        return smtp_conntection.wyslij(temat, tresc, adresat)
        # print(res)