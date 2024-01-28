from .KontoOsobiste import KontoOsobiste
from pymongo import MongoClient

class RejestrKont():
    client = MongoClient('localhost', 27017)
    db = client['bank_baza']
    collection = db['konta']
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

    @classmethod
    def load(cls):
        cls.lista_kont = []
        for konto in cls.collection.find({}):
            nowe_konto = KontoOsobiste(konto["imie"], konto["nazwisko"], konto['pesel'])
            nowe_konto.history = konto['history']
            nowe_konto.saldo = konto['saldo']
            cls.lista_kont.append(nowe_konto)

    @classmethod
    def save(cls):
        cls.collection.delete_many({})
        for konto in cls.lista_kont:
            cls.collection.insert_one({ "imie": konto.imie, "nazwisko": konto.nazwisko, 
                                   "saldo": konto.saldo, "pesel": konto.pesel, 
                                   "history": konto.history })
