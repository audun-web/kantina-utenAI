from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def meny():
    menyliste = [
        {"dag": "Mandag", "rett": "Pizza", "allergener": "Gluten", "pris": "20kr"},
        {"dag": "Tirsdag", "rett": "Fried Chicken", "allergener": "Melk", "pris": "25kr"},
        {"dag": "Onsdag", "rett": "Stekt Laks med Poteter", "allergener": "Talerken", "pris": "30kr"},
        {"dag": "Torsdag", "rett": "Stekt Ris", "allergener": "Ris", "pris": "20kr"},
        {"dag": "Fredag", "rett": "Taco", "allergener": "Mexikanere", "pris": "25kr"}
    ]
    return render_template('meny.html', menyliste=menyliste)

@app.route('/varer')
def varer():
    return render_template('varer.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)