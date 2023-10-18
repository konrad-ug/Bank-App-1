class Konto:
    def __init__(self):
        self.express_transfer_fee = 0
        self.saldo = 0
 
    def zaksięguj_przelew_przychodzący(self, kwota):
        if kwota > 0:
            self.saldo += kwota

    def przelew_wychodzący(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota

    def przelew_wychodzący_ekspresowy(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota
            self.saldo -= self.express_transfer_fee