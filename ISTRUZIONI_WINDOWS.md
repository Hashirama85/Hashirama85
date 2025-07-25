# 🏭 Gestionale Magazzino Spezie - Windows 10/11

Un sistema completo per la gestione del magazzino di spezie e ingredienti con tracciabilità dei lotti.

## 🚀 CREAZIONE ESEGUIBILE - ISTRUZIONI RAPIDE

### Passo 1: Requisiti
Assicurati di avere installato:
- **Windows 10** (versione 1903+) o **Windows 11**
- **Python 3.8 o superiore** → [Scarica qui](https://www.python.org/downloads/)
  - ⚠️ **IMPORTANTE**: Durante l'installazione di Python, seleziona "Add Python to PATH"

### Passo 2: Download del Progetto
1. Scarica tutti i file del progetto in una cartella
2. Assicurati che la cartella contenga:
   - `app.py`
   - `requirements.txt`
   - `create_executable.bat`
   - Cartelle `templates/` e `static/`

### Passo 3: Creazione dell'Eseguibile
1. **Fai doppio clic** su `create_executable.bat`
2. **Attendi** 5-15 minuti (il processo è automatico)
3. **L'eseguibile** sarà creato nella cartella `dist/`

## 📦 CONTENUTO DELL'ESEGUIBILE

Dopo la creazione troverai nella cartella `dist/`:
- **GestionaleMagazzinoSpezie.exe** (l'applicazione)
- **README.txt** (guida per l'utente finale)

## 🖥️ UTILIZZO DEL PROGRAMMA

### Avvio del Gestionale
1. Fai **doppio clic** su `GestionaleMagazzinoSpezie.exe`
2. Attendi 2-5 secondi per l'avvio
3. Il **browser si aprirà automaticamente**
4. Se il browser non si apre, vai su: `http://localhost:5000`

### Interfaccia Web
Il programma si presenta come un sito web moderno con:
- **Dashboard** principale con riepilogo magazzino
- **Menu di navigazione** sempre visibile
- **Design responsive** (funziona anche su tablet)

## ⚙️ FUNZIONALITÀ PRINCIPALI

### 🏷️ Gestione Prodotti
- **Aggiungi prodotti** (spezie, ingredienti, ecc.)
- **Definisci unità di misura** (kg, g, L, ml, pz, conf, ecc.)
- **Elimina prodotti** non più utilizzati

### 📦 Gestione Lotti
- **Lotti multipli** per ogni prodotto
- **Codici lotto** personalizzati o auto-generati
- **Date di scadenza** per tracciabilità
- **Controllo automatico** delle scadenze

### 📊 Operazioni di Magazzino
- **Carico merce** con controllo quantità
- **Scarico merce** con verifica disponibilità
- **Principio FIFO** (First In, First Out)
- **Note personalizzabili** per ogni movimento

### 📈 Reportistica e Analisi
- **Dashboard** con statistiche in tempo reale
- **Storico movimenti** completo e filtrato
- **Esportazione CSV** dei dati
- **Filtri avanzati** per data, prodotto, tipo movimento

## 🔧 CONFIGURAZIONE E PERSONALIZZAZIONE

### Modifica Unità di Misura
Per aggiungere nuove unità di misura:
1. Apri `templates/nuovo_prodotto.html` con un editor di testo
2. Trova la sezione `<select>` con le unità
3. Aggiungi: `<option value="tua_unita">Tua Unità (tu)</option>`

### Cambio Porta di Accesso
Se la porta 5000 è occupata:
1. Apri `app.py` con un editor di testo
2. Cerca `port = 5000`
3. Cambia con `port = 8080` (o altra porta libera)

## 💾 GESTIONE DATI

### File di Database
- I dati sono salvati in `magazzino_data.json`
- Il file si crea automaticamente al primo utilizzo
- **Mantieni sempre questo file insieme all'eseguibile**

### Backup dei Dati
⚠️ **IMPORTANTE**: Fai backup regolari!
1. Copia il file `magazzino_data.json`
2. Salvalo in un posto sicuro (cloud, USB, ecc.)
3. In caso di problemi, sostituisci il file per ripristinare i dati

### Ripristino Dati
Per trasferire i dati su un altro computer:
1. Copia `GestionaleMagazzinoSpezie.exe` sul nuovo computer
2. Copia anche `magazzino_data.json` nella stessa cartella
3. Avvia il programma normalmente

## 🖱️ GUIDE D'USO

### Primo Utilizzo
1. **Avvia il programma**
2. **Aggiungi il primo prodotto** (es: "Pepe Nero", unità "g")
3. **Effettua un carico** (es: Lotto "PEP-240101", 500g, scadenza 2025-12-31)
4. **Verifica il dashboard** per vedere le statistiche

### Operazione di Carico
1. Menu → **Carico**
2. Seleziona il **prodotto**
3. Inserisci **codice lotto** (o usa "Auto")
4. Inserisci **quantità** e **data scadenza**
5. Aggiungi **note** se necessario
6. Clicca **"Registra Carico"**

### Operazione di Scarico
1. Menu → **Scarico**
2. Seleziona il **prodotto** (solo quelli con scorte)
3. Scegli il **lotto** da scaricare
4. Inserisci la **quantità** (max = disponibile)
5. Aggiungi **note** sul motivo dello scarico
6. Clicca **"Registra Scarico"**

### Visualizzazione Movimenti
1. Menu → **Movimenti**
2. Usa i **filtri** per cercare:
   - Per tipo (carico/scarico)
   - Per prodotto
   - Per periodo di date
3. **Esporta in CSV** per analisi esterne

## 🐛 RISOLUZIONE PROBLEMI

### Il programma non si avvia
- **Antivirus**: Aggiungi l'eseguibile alle eccezioni
- **Amministratore**: Prova ad eseguire come amministratore
- **Porta occupata**: Chiudi altre istanze del programma

### Il browser non si apre
- Apri manualmente il browser
- Vai su: `http://localhost:5000`
- Verifica che il programma sia in esecuzione (icona nella taskbar)

### Errore "Porta già in uso"
- Chiudi tutte le istanze del programma
- Riavvia il computer
- Cambia porta nel file `app.py` come spiegato sopra

### Perdita di dati
- Verifica che `magazzino_data.json` sia presente
- Ripristina da backup se disponibile
- I dati si salvano automaticamente ad ogni operazione

### Problemi di performance
- Chiudi altri programmi pesanti
- Verifica almeno 4GB di RAM disponibile
- Pulisci i file temporanei di Windows

## 🔒 SICUREZZA E PRIVACY

### Dati Locali
- **Tutti i dati rimangono sul tuo computer**
- **Nessuna trasmissione online**
- **Privacy completa** delle informazioni aziendali

### Accesso alla Rete
Il programma usa solo:
- **Porta locale 5000** per l'interfaccia web
- **Nessun accesso esterno** a internet
- **Nessun invio dati** a server esterni

### Antivirus
Alcuni antivirus potrebbero segnalare falsi positivi:
- **Aggiungi eccezione** per l'eseguibile
- È normale per file creati con PyInstaller
- Il codice sorgente è disponibile per verifica

## 📱 ACCESSO DA ALTRI DISPOSITIVI

### Rete Locale
Per accedere da tablet/altri PC nella stessa rete:
1. Modifica `app.py`: cambia `host='127.0.0.1'` in `host='0.0.0.0'`
2. Ricompila l'eseguibile
3. Gli altri dispositivi potranno accedere tramite IP del PC

### Sicurezza Rete
⚠️ **Attenzione**: L'accesso da rete è senza password
- Usa solo in reti private/aziendali sicure
- Non esporre su internet pubblico

## 📊 SPECIFICHE TECNICHE

### Requisiti di Sistema
| Componente | Minimo | Consigliato |
|------------|---------|-------------|
| OS | Windows 10 1903+ | Windows 11 |
| RAM | 4 GB | 8 GB |
| Spazio disco | 100 MB | 500 MB |
| Processore | Dual Core | Quad Core |

### Performance
| Metrica | Valore |
|---------|--------|
| Tempo avvio | 2-5 secondi |
| RAM utilizzata | 50-80 MB |
| Dimensione eseguibile | ~45-60 MB |
| Database crescita | ~1KB per movimento |

### Browser Supportati
- ✅ **Chrome/Edge** (Consigliato)
- ✅ **Firefox**
- ✅ **Safari**
- ⚠️ **Internet Explorer** (limitato)

## 🆘 SUPPORTO

### Auto-Diagnosi
1. Verifica i **requisiti di sistema**
2. Controlla i **file di log** nella console
3. Prova a **riavviare** il programma
4. Verifica **spazio libero** su disco

### File di Log
Il programma mostra errori nella finestra di comando:
- Tieni aperta la finestra per vedere eventuali errori
- Copia i messaggi di errore per la risoluzione

### Backup di Emergenza
In caso di problemi gravi:
1. **Salva** il file `magazzino_data.json`
2. **Reinstalla** il programma
3. **Ripristina** il file dati

## 📄 NOTE LEGALI

### Licenza d'Uso
- Software fornito **"così com'è"**
- Uso **personale e commerciale** consentito
- **Nessuna garanzia** esplicita o implicita

### Responsabilità
- L'utente è responsabile del **backup dei dati**
- **Nessuna responsabilità** per perdite di dati
- Testare sempre prima dell'uso in produzione

---

## 📞 INFORMAZIONI DI SUPPORTO

**Software**: Gestionale Magazzino Spezie  
**Versione**: 1.0.0  
**Compatibilità**: Windows 10/11  
**Tipo**: Applicazione desktop con interfaccia web  
**Linguaggio**: Python + HTML/CSS/JavaScript

🚀 **Buon lavoro con il tuo nuovo gestionale magazzino!**