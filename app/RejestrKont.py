from .Konto import Konto

class RejestrKont():
    lista = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista.append(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.lista)

    @classmethod
    def znajdź_konto(cls, szukany_pesel):
        for konto in lista_kont:
            if konto.pesel == szukany_pesel:
                return konto
        return None