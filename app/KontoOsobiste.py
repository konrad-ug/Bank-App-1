from .Konto import Konto

class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko, pesel, promo_code = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.express_transfer_fee = 1
        self.history = []
        self.email_msg = "Twoja historia konta to"

        if self.is_pesel_correct(pesel):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if self.is_promo_code_correct(promo_code) and self.is_person_qualified_for_promotion(pesel):
            self.saldo = 50
        else:
            self.saldo = 0

    def is_pesel_correct(self, pesel):
        if len(pesel) != 11:
            return False
        
        if not pesel.isdigit():
            return False
        
        return True


    def is_promo_code_correct(self, promo_code):
        if promo_code is None:
            return False
        if promo_code.startswith("PROM_") and len(promo_code) == 8:
            return True
        return False

    def is_person_qualified_for_promotion(self, pesel):
        if pesel[2] == "2" or pesel[3] == "3":
            return True
        elif pesel[0:2] > "60":
            return True
        return False
    
    
    def czy_n_ostatnich_to_wpłaty(self, n):
        if len(self.history) >= n and all(element > 0 for element in self.history[-n:]):
            return True
        return False
    
    def czy_n_ostatnich_większe_od_kwoty(self, n, kwota):
        if len(self.history) >= n and sum(self.history[-n:]) > kwota:
            return True
        return False 

    def zaciagnij_kredyt(self, kwota):
        if self.czy_n_ostatnich_większe_od_kwoty(5, kwota) or self.czy_n_ostatnich_to_wpłaty(3):
            self.saldo += kwota
            return True
        return False


