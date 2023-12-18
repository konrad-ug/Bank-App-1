from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste
from app.Konto import Konto

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
   dane = request.get_json()
   print(f"Request o stworzenie konta z danymi: {dane}")
   if RejestrKont.znajdź_konto(dane["pesel"]) != None:
      return jsonify({"message": "Konto już istnieje!"}), 409
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

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def wykonaj_przelew(pesel):
   request_data = request.get_json()
   znalezione_konto = RejestrKont.znajdź_konto(str(pesel))
   if znalezione_konto == None:
      return jsonify({"message": "brak konta o podanym peselu"}), 404
   else:
      if request_data["type"] == "incoming":
         znalezione_konto.zaksięguj_przelew_przychodzący(request_data["amount"])
         return jsonify({"messasge": "pomyślnie zaksięgowano przelew przychodzący"}), 200

      elif request_data["type"] == "outgoing":
         if znalezione_konto.saldo >= request_data["amount"]:
            znalezione_konto.przelew_wychodzący(request_data["amount"])
            return jsonify({"messasge": "pomyślnie zaksięgowano przelew przychodzący"}), 200
         return jsonify({"message": "niewystarczające środki na koncie"}), 422
      else:
         return jsonify({"messasge": "nieprawidłowy typ przelewu"}), 404

   @app.route("/api/accounts/save", methods=['PATCH'])
   def save_to_db():
      RejestrKont.save()
      return jsonify({"message": "accounts were saved to db"})

   @app.route("/api/accounts/load", methods=['PATCH'])
   def load_to_db():
      RejestrKont.load()
      return jsonify({"message": "accounts loaded from db"})
   
