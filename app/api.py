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
    return jsonify({"liczba_kont": "wynik"}), 201


@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
   dane = request.get_json()
   return dane, 200


