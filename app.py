from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def meny():
    menyliste = [
        {"dag": "Mandag", "rett": "Pizza", "allergener": "Gluten", "pris": "20kr", "bilde": "pizza.avif"},
        {"dag": "Tirsdag", "rett": "Fried Chicken", "allergener": "Melk og hvite folk", "pris": "25kr", "bilde": "fried-chicken.jpg"},
        {"dag": "Onsdag", "rett": "Stekt Laks med Poteter", "allergener": "Talerken", "pris": "30kr", "bilde": "stekt-laks.png"},
        {"dag": "Torsdag", "rett": "Stekt Ris", "allergener": "Ris", "pris": "20kr", "bilde": "stekt-ris.png"},
        {"dag": "Fredag", "rett": "Taco", "allergener": "Mexikanere", "pris": "25kr", "bilde": "taco.png"}
    ]
    # Henter dagens ukedag som et tall (Mandag=0, Tirsdag=1, etc.)
    today_index = datetime.now().weekday()
    return render_template('meny.html', menyliste=menyliste, today=today_index)

@app.route('/varer')
def varer():
    vareliste = [
        {"navn": "Monster", "pris": "30kr", "bilde": "monster.png"},
        {"navn": "Pepsi", "pris": "15kr", "bilde": "pepsi.png"},
        {"navn": "Sandwich", "pris": "15kr", "bilde": "sandwich.png"},
        {"navn": "ProteinShake", "pris": "15kr", "bilde": "proteinshake.png"},
        {"navn": "Kaffe", "pris": "25kr", "bilde": "kaffe.png"}
    ]
    return render_template('varer.html', vareliste=vareliste)

@app.route('/kontakt')
def kontakt():
    kontaktliste = [
        {"navn": "Audun Midtgård Meckelborg", "stilling": "CEO", "tlf": "+47 123 45 678", "bilde": "audun.png"},
        {"navn": "Ebbe Gaston Zelow", "stilling": "Salgsperson", "tlf": "+48 123 45 678", "bilde": "ebbe.png"},
        {"navn": "Ludvig Meland Egeberg", "stilling": "Kokk", "tlf": "+49 123 45 678", "bilde": "ludvig.png"},
        {"navn": "Nikolai Hauke Westergaard", "stilling": "Vaskedame", "tlf": "+50 123 45 678", "bilde": "nikolai.png"}
    ]
    return render_template('kontakt.html', kontaktliste=kontaktliste)

if __name__ == '__main__':
    app.run(debug=True)