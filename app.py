from flask import Flask, render_template

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
    return render_template('meny.html', menyliste=menyliste)

@app.route('/varer')
def varer():
    vareliste = [
        {"navn": "Monster", "pris": "30kr", "bilde": "monster.png"},
        {"navn": "Pepsi", "pris": "15kr", "bilde": "pepsi.png"},
        {"navn": "Sandwich", "pris": "15kr", "bilde": "sandwich.png"},
        {"navn": "ProteinShake", "pris": "15kr", "bilde": "proteinshake.png"},
        {"navn": "Kaffe", "pris": "25kr", "bilde": "kaffe.png"}
    ]
    return render_template('varer.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)