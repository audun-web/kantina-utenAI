from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def meny():
    menyliste = [
        {"dag": "Mandag", "rett": "Stekt Ludvig", "allergener": "Gul Caps"},
        {"dag": "Tirsdag", "rett": "Stekt Ebbe", "allergener": "Discord"},
        {"dag": "Onsdag", "rett": "Stekt Niko", "allergener": "Kattehår"},
        {"dag": "Torsdag", "rett": "Stekt Lis", "allergener": "Egg"},
        {"dag": "Fredag", "rett": "Taco", "allergener": "Mexikanere"}
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