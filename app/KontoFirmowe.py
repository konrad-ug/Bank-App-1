from .Konto import Konto

class KontoFirmowe(Konto):
    express_transfer_fee = 5


    def __init__(self, name, nip):
        self.name = name
        self.saldo = 0
        self.history = []
        
        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        
        else:
            self.nip = nip

    def zaciagnij_kredyt(self, kwota):
        if self.saldo >= 2 * kwota and -1775 in self.history:
            self.saldo += kwota
            return True
        return False

