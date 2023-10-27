class Konto:
    def __init__(self):
        self.express_transfer_fee = 0
        self.saldo = 0
        self.history = []
 
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