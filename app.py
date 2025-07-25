from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import os
import webbrowser
import threading
import time
import sys

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

def open_browser():
    """Apre il browser automaticamente dopo un breve ritardo"""
    time.sleep(1.5)  # Attende che il server si avvii
    try:
        webbrowser.open('http://localhost:5000')
    except:
        pass  # Se non riesce ad aprire il browser, continua comunque

def is_port_in_use(port):
    """Verifica se una porta è già in uso"""
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if __name__ == '__main__':
    # Determina se siamo in un eseguibile PyInstaller
    if getattr(sys, 'frozen', False):
        # Siamo in un eseguibile
        debug_mode = False
        # Avvia il browser automaticamente
        threading.Thread(target=open_browser, daemon=True).start()
        
        print("🚀 Gestionale Magazzino Spezie avviato!")
        print("📱 Il browser si aprirà automaticamente...")
        print("🌐 Se il browser non si apre, vai manualmente su: http://localhost:5000")
        print("❌ Per chiudere il programma, chiudi questa finestra")
        print("-" * 60)
    else:
        # Siamo in modalità sviluppo
        debug_mode = True
        print("🔧 Modalità sviluppo attiva")
    
    # Verifica che la porta non sia già in uso
    port = 5000
    if is_port_in_use(port):
        print(f"⚠️  Porta {port} già in uso. Prova a chiudere altre istanze del programma.")
        if getattr(sys, 'frozen', False):
            input("Premi INVIO per uscire...")
            sys.exit(1)
    
    try:
        app.run(debug=debug_mode, host='127.0.0.1', port=port, use_reloader=False)
    except KeyboardInterrupt:
        print("\n👋 Gestionale Magazzino Spezie chiuso")
    except Exception as e:
        print(f"❌ Errore: {e}")
        if getattr(sys, 'frozen', False):
            input("Premi INVIO per uscire...")
            sys.exit(1)