class Konto:
    def __init__(self, imie, nazwisko, pesel, promo_code = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0

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
        
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        control_digit = 10 - sum(int((pesel[i]) * weights[i]) % 10 for i in range(10)) % 10

        if int(pesel[10]) == control_digit:
            return True
        return False


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