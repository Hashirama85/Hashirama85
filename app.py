from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)

# File per memorizzare i dati
DATA_FILE = 'magazzino_data.json'

def load_data():
    """Carica i dati dal file JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'prodotti': {},
        'movimenti': []
    }

def save_data(data):
    """Salva i dati nel file JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Pagina principale con la lista dei prodotti e rimanenze"""
    data = load_data()
    return render_template('index.html', prodotti=data['prodotti'])

@app.route('/nuovo_prodotto', methods=['GET', 'POST'])
def nuovo_prodotto():
    """Aggiunge un nuovo prodotto"""
    if request.method == 'POST':
        data = load_data()
        nome_prodotto = request.form['nome_prodotto']
        unita_misura = request.form['unita_misura']
        
        if nome_prodotto not in data['prodotti']:
            data['prodotti'][nome_prodotto] = {
                'unita_misura': unita_misura,
                'lotti': {}
            }
            save_data(data)
        
        return redirect(url_for('index'))
    
    return render_template('nuovo_prodotto.html')

@app.route('/carico', methods=['GET', 'POST'])
def carico():
    """Gestisce il carico di merce"""
    data = load_data()
    
    if request.method == 'POST':
        prodotto = request.form['prodotto']
        lotto = request.form['lotto']
        quantita = float(request.form['quantita'])
        data_scadenza = request.form['data_scadenza']
        note = request.form.get('note', '')
        
        # Aggiorna il lotto
        if lotto not in data['prodotti'][prodotto]['lotti']:
            data['prodotti'][prodotto]['lotti'][lotto] = {
                'quantita': 0,
                'data_scadenza': data_scadenza,
                'data_creazione': datetime.now().isoformat()
            }
        
        data['prodotti'][prodotto]['lotti'][lotto]['quantita'] += quantita
        
        # Registra il movimento
        movimento = {
            'timestamp': datetime.now().isoformat(),
            'tipo': 'carico',
            'prodotto': prodotto,
            'lotto': lotto,
            'quantita': quantita,
            'note': note
        }
        data['movimenti'].append(movimento)
        
        save_data(data)
        return redirect(url_for('index'))
    
    return render_template('carico.html', prodotti=data['prodotti'])

@app.route('/scarico', methods=['GET', 'POST'])
def scarico():
    """Gestisce lo scarico di merce"""
    data = load_data()
    
    if request.method == 'POST':
        prodotto = request.form['prodotto']
        lotto = request.form['lotto']
        quantita = float(request.form['quantita'])
        note = request.form.get('note', '')
        
        # Verifica disponibilità
        if (prodotto in data['prodotti'] and 
            lotto in data['prodotti'][prodotto]['lotti'] and 
            data['prodotti'][prodotto]['lotti'][lotto]['quantita'] >= quantita):
            
            # Aggiorna il lotto
            data['prodotti'][prodotto]['lotti'][lotto]['quantita'] -= quantita
            
            # Registra il movimento
            movimento = {
                'timestamp': datetime.now().isoformat(),
                'tipo': 'scarico',
                'prodotto': prodotto,
                'lotto': lotto,
                'quantita': quantita,
                'note': note
            }
            data['movimenti'].append(movimento)
            
            save_data(data)
            return redirect(url_for('index'))
        else:
            return render_template('scarico.html', prodotti=data['prodotti'], 
                                 errore="Quantità non disponibile per questo lotto")
    
    return render_template('scarico.html', prodotti=data['prodotti'])

@app.route('/movimenti')
def movimenti():
    """Visualizza lo storico dei movimenti"""
    data = load_data()
    movimenti_ordinati = sorted(data['movimenti'], 
                               key=lambda x: x['timestamp'], reverse=True)
    return render_template('movimenti.html', movimenti=movimenti_ordinati)

@app.route('/api/lotti/<prodotto>')
def api_lotti(prodotto):
    """API per ottenere i lotti di un prodotto"""
    data = load_data()
    if prodotto in data['prodotti']:
        return jsonify(data['prodotti'][prodotto]['lotti'])
    return jsonify({})

@app.route('/elimina_prodotto/<prodotto>', methods=['POST'])
def elimina_prodotto(prodotto):
    """Elimina un prodotto"""
    data = load_data()
    if prodotto in data['prodotti']:
        del data['prodotti'][prodotto]
        save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)