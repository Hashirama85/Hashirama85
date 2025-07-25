# Gestionale Magazzino Spezie - Guida alla Creazione dell'Eseguibile Windows

Un sistema completo per la gestione del magazzino di spezie e ingredienti con tracciabilità dei lotti, compatibile con Windows 10 e 11.

## 🚀 Creazione Rapida dell'Eseguibile

### Metodo 1: File Batch (Consigliato)
1. Fai doppio clic su `build_windows_exe.bat`
2. Attendi il completamento (3-10 minuti)
3. L'eseguibile sarà nella cartella `dist/`

### Metodo 2: Manuale
```bash
# 1. Installa le dipendenze
pip install -r requirements.txt

# 2. Esegui lo script di build
python build_exe.py
```

## 📋 Requisiti di Sistema per la Creazione

- **Windows 10/11** (per creare l'eseguibile)
- **Python 3.8+** installato
- **pip** aggiornato
- **4 GB RAM** minimo
- **1 GB spazio libero** per la compilazione

## 📦 Struttura del Progetto

```
gestionale-magazzino-spezie/
├── app.py                    # Applicazione Flask principale
├── requirements.txt          # Dipendenze Python
├── build_exe.py             # Script per creare l'eseguibile
├── build_windows_exe.bat    # File batch per Windows
├── templates/               # Template HTML
│   ├── base.html
│   ├── index.html
│   ├── nuovo_prodotto.html
│   ├── carico.html
│   ├── scarico.html
│   └── movimenti.html
├── static/                  # File statici
│   ├── css/style.css
│   └── js/app.js
└── dist/                    # Cartella eseguibile (creata dal build)
    ├── GestionaleMagazzinoSpezie.exe
    └── README.txt
```

## ⚙️ Funzionalità del Gestionale

### ✅ Gestione Prodotti
- Aggiunta/rimozione prodotti
- Definizione unità di misura
- Categorizzazione spezie/ingredienti

### 📦 Gestione Lotti
- Lotti multipli per prodotto
- Codici lotto personalizzati o auto-generati
- Date di scadenza per ogni lotto
- Principio FIFO (First In, First Out)

### 📊 Carico e Scarico
- Interfaccia intuitiva per operazioni
- Controllo automatico disponibilità
- Note personalizzabili per ogni movimento
- Validazione quantità in tempo reale

### 📈 Tracciabilità e Reportistica
- Storico completo movimenti
- Filtri avanzati per ricerca
- Esportazione dati in CSV
- Dashboard con statistiche

### 🔒 Sicurezza e Backup
- Dati salvati localmente (JSON)
- Non richiede connessione internet
- Backup automatico consigliato
- Nessun dato sensibile in cloud

## 🖥️ Compatibilità

### Windows
- ✅ **Windows 10** (versione 1903+)
- ✅ **Windows 11** (tutte le versioni)
- ✅ **32-bit e 64-bit**

### Browser Supportati
- ✅ Chrome/Edge (Consigliato)
- ✅ Firefox
- ✅ Safari
- ⚠️ Internet Explorer (limitato)

## 🛠️ Personalizzazione

### Modifica Unità di Misura
Modifica il file `templates/nuovo_prodotto.html` nella sezione select delle unità:

```html
<option value="nuova_unita">Nuova Unità (nu)</option>
```

### Cambio Porta di Default
Modifica in `app.py`:

```python
port = 5000  # Cambia con la porta desiderata
```

### Stili Personalizzati
Modifica `static/css/style.css` per personalizzare l'aspetto.

## 🐛 Risoluzione Problemi

### PyInstaller Non Si Installa
```bash
python -m pip install --upgrade pip
python -m pip install pyinstaller==6.3.0
```

### Errore "Porta Già in Uso"
- Chiudi altre istanze del programma
- Riavvia il computer
- Cambia porta in `app.py`

### Eseguibile Non Si Avvia
- Verifica antivirus (aggiungi eccezione)
- Esegui come amministratore
- Controlla log errori nella console

### Browser Non Si Apre Automaticamente
Vai manualmente su: `http://localhost:5000`

## 📊 Dimensioni e Performance

| Componente | Dimensione |
|------------|------------|
| Eseguibile finale | ~45-60 MB |
| Tempo avvio | 2-5 secondi |
| RAM utilizzata | ~50-80 MB |
| Storage dati | ~1-10 MB |

## 🔧 Sviluppo e Contributi

### Avvio in Modalità Sviluppo
```bash
python app.py
```

### Struttura Codice
- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5 + JavaScript vanilla
- **Database**: JSON file locale
- **Build**: PyInstaller

## 📝 Note Importanti

### ⚠️ Backup Dati
- Il file `magazzino_data.json` contiene tutti i dati
- Fai backup regolari di questo file
- Tieni il file nella stessa cartella dell'eseguibile

### 🔒 Sicurezza
- I dati rimangono locali al computer
- Nessuna trasmissione online
- Password non richieste (uso locale)

### 📱 Utilizzo Mobile
- Responsive design funziona su tablet
- Accesso da rete locale possibile
- Non ottimizzato per smartphone piccoli

## 🆘 Supporto

Per problemi o suggerimenti:
1. Controlla questo README
2. Verifica i log di errore
3. Riavvia il programma
4. Verifica compatibilità sistema

## 📜 Licenza

Questo software è fornito "così com'è" per uso personale e commerciale.
Mantieni il file README insieme all'eseguibile per riferimenti futuri.

---

**Versione**: 1.0.0  
**Data**: 2024  
**Compatibilità**: Windows 10/11  
**Linguaggio**: Python + HTML/CSS/JS