from .Konto import Konto

class RejestrKont():
    lista_kont = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista_kont.append(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.lista_kont)

    @classmethod
    def znajdź_konto(cls, szukany_pesel):
        for konto in cls.lista_kont:
            if str(konto.pesel) == str(szukany_pesel):
                return konto
        return None