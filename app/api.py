from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
   dane = request.get_json()
   print(f"Request o stworzenie konta z danymi: {dane}")
   konto = KontoOsobiste(dane["imie"], dane["nazwisko"], dane["pesel"])
   RejestrKont.dodaj_konto(konto)
   return jsonify({"message": "Konto stworzone"}), 201


@app.route("/api/accounts/count", methods=['GET'])
def ile_kont():
    wynik=RejestrKont.ile_kont()
    print(wynik)
    return jsonify({"liczba_kont": wynik}), 200


@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
   wynik = RejestrKont.znajdź_konto(str(pesel))
   print("z geta przez pesel", wynik)
   if wynik != None:
      return jsonify({"imie": wynik.imie, "nazwisko": wynik.nazwisko, "pesel": str(wynik.pesel), "saldo": wynik.saldo }), 200
   return jsonify({"message": "brak konta o podanym peselu"}), 404


@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
   znalezione_konto = RejestrKont.znajdź_konto(str(pesel))
   if znalezione_konto != None:
      RejestrKont.lista_kont.remove(znalezione_konto)
      return jsonify({"message": "usunięto konto pomyślnie"}), 200
   return jsonify({"message": "brak konta o podanym peselu"}), 404
   

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def zmodyfikuj_konto(pesel):
   request_data = request.get_json()
   znalezione_konto = RejestrKont.znajdź_konto(str(pesel))
   print(request_data)
   if znalezione_konto == None:
      return jsonify({"message": "brak konta o podanym peselu"}), 404
   
   for key, value in request_data.items():
      if key in ["saldo", "imie", "nazwisko", "pesel"]:
         setattr(znalezione_konto, key, value)
         print(key, getattr(znalezione_konto, key))
   
   return jsonify({"message": "zakutalizowano pomyślnie"}), 200


