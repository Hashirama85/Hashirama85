@echo off
setlocal

title Gestionale Magazzino Spezie - Creazione Eseguibile
color 0B

echo.
echo =====================================================
echo    GESTIONALE MAGAZZINO SPEZIE
echo    Creatore di Eseguibile per Windows 10/11
echo =====================================================
echo.

:: Verifica Python
echo [1/6] Verifica installazione Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ ERRORE: Python non trovato!
    echo.
    echo Per creare l'eseguibile devi installare Python:
    echo 🔗 https://www.python.org/downloads/
    echo.
    echo Assicurati di selezionare "Add Python to PATH" durante l'installazione
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% trovato

:: Crea ambiente virtuale
echo.
echo [2/6] Creazione ambiente virtuale...
if exist "venv" rmdir /s /q venv
python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ Errore nella creazione dell'ambiente virtuale
    pause
    exit /b 1
)
echo ✅ Ambiente virtuale creato

:: Attiva ambiente virtuale
echo.
echo [3/6] Attivazione ambiente virtuale...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ Errore nell'attivazione dell'ambiente virtuale
    pause
    exit /b 1
)
echo ✅ Ambiente virtuale attivato

:: Aggiorna pip
echo.
echo [4/6] Aggiornamento pip...
python -m pip install --upgrade pip --quiet
echo ✅ pip aggiornato

:: Installa dipendenze
echo.
echo [5/6] Installazione dipendenze...
echo Installazione in corso... (potrebbe richiedere alcuni minuti)
python -m pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo ❌ Errore nell'installazione delle dipendenze
    pause
    exit /b 1
)
echo ✅ Dipendenze installate

:: Crea eseguibile
echo.
echo [6/6] Creazione eseguibile...
echo.
echo 🚀 Inizio processo di compilazione...
echo ⏳ Questo processo richiederà 3-10 minuti, attendi...
echo.

:: Pulisci directory precedenti
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build

:: Crea file spec per PyInstaller
echo # -*- mode: python ; coding: utf-8 -*- > app.spec
echo. >> app.spec
echo a = Analysis( >> app.spec
echo     ['app.py'], >> app.spec
echo     pathex=[], >> app.spec
echo     binaries=[], >> app.spec
echo     datas=[ >> app.spec
echo         ('templates', 'templates'), >> app.spec
echo         ('static', 'static'), >> app.spec
echo     ], >> app.spec
echo     hiddenimports=[ >> app.spec
echo         'flask', >> app.spec
echo         'werkzeug', >> app.spec
echo         'jinja2', >> app.spec
echo         'markupsafe', >> app.spec
echo         'itsdangerous', >> app.spec
echo         'click', >> app.spec
echo         'blinker', >> app.spec
echo     ], >> app.spec
echo     hookspath=[], >> app.spec
echo     runtime_hooks=[], >> app.spec
echo     excludes=[], >> app.spec
echo     noarchive=False, >> app.spec
echo ^) >> app.spec
echo. >> app.spec
echo pyz = PYZ(a.pure, a.zipped_data) >> app.spec
echo. >> app.spec
echo exe = EXE( >> app.spec
echo     pyz, >> app.spec
echo     a.scripts, >> app.spec
echo     a.binaries, >> app.spec
echo     a.zipfiles, >> app.spec
echo     a.datas, >> app.spec
echo     [], >> app.spec
echo     name='GestionaleMagazzinoSpezie', >> app.spec
echo     debug=False, >> app.spec
echo     bootloader_ignore_signals=False, >> app.spec
echo     strip=False, >> app.spec
echo     upx=True, >> app.spec
echo     console=True, >> app.spec
echo     disable_windowed_traceback=False, >> app.spec
echo ^) >> app.spec

:: Esegui PyInstaller
pyinstaller --clean --noconfirm app.spec
if %errorlevel% neq 0 (
    echo.
    echo ❌ Errore durante la creazione dell'eseguibile
    echo.
    echo Possibili soluzioni:
    echo - Disattiva temporaneamente l'antivirus
    echo - Esegui come amministratore
    echo - Verifica spazio libero su disco (minimo 1GB)
    echo.
    pause
    exit /b 1
)

:: Verifica che l'eseguibile sia stato creato
if not exist "dist\GestionaleMagazzinoSpezie.exe" (
    echo ❌ Eseguibile non trovato dopo la compilazione
    pause
    exit /b 1
)

:: Crea README per l'utente finale
echo # Gestionale Magazzino Spezie > dist\README.txt
echo. >> dist\README.txt
echo ## Come utilizzare il programma >> dist\README.txt
echo. >> dist\README.txt
echo 1. Fai doppio clic su 'GestionaleMagazzinoSpezie.exe' >> dist\README.txt
echo 2. Attendi che si apra automaticamente il browser >> dist\README.txt
echo 3. Se il browser non si apre, vai su: http://localhost:5000 >> dist\README.txt
echo. >> dist\README.txt
echo ## Funzionalità principali >> dist\README.txt
echo. >> dist\README.txt
echo - Gestione prodotti (spezie/ingredienti) >> dist\README.txt
echo - Carico e scarico con controllo lotti >> dist\README.txt
echo - Tracciabilità completa dei movimenti >> dist\README.txt
echo - Controllo automatico delle scadenze >> dist\README.txt
echo - Principio FIFO (First In, First Out) >> dist\README.txt
echo - Dashboard con statistiche >> dist\README.txt
echo - Esportazione dati in CSV >> dist\README.txt
echo. >> dist\README.txt
echo ## IMPORTANTE - Backup dei dati >> dist\README.txt
echo. >> dist\README.txt
echo Il file 'magazzino_data.json' contiene tutti i tuoi dati. >> dist\README.txt
echo Fai backup regolari di questo file! >> dist\README.txt
echo. >> dist\README.txt
echo ## Requisiti di sistema >> dist\README.txt
echo. >> dist\README.txt
echo - Windows 10 (versione 1903 o superiore) >> dist\README.txt
echo - Windows 11 (tutte le versioni) >> dist\README.txt
echo - 4 GB di RAM minimo >> dist\README.txt
echo - Browser web moderno (Chrome, Edge, Firefox) >> dist\README.txt
echo. >> dist\README.txt
echo Versione: 1.0.0 >> dist\README.txt
echo Data build: %date% >> dist\README.txt

:: Calcola dimensione file
for %%A in (dist\GestionaleMagazzinoSpezie.exe) do set SIZE=%%~zA
set /a SIZE_MB=%SIZE%/1048576

:: Pulisci file temporanei
del app.spec >nul 2>&1
rmdir /s /q build >nul 2>&1

:: Disattiva ambiente virtuale
call venv\Scripts\deactivate.bat

echo.
echo ================================================================
echo               🎉 ESEGUIBILE CREATO CON SUCCESSO! 🎉
echo ================================================================
echo.
echo 📦 File creato: dist\GestionaleMagazzinoSpezie.exe
echo 📏 Dimensione: ~%SIZE_MB% MB
echo 📂 Cartella: %CD%\dist\
echo.
echo 📋 File inclusi nella cartella 'dist':
echo    ✅ GestionaleMagazzinoSpezie.exe (applicazione principale)
echo    ✅ README.txt (guida all'uso)
echo.
echo 💡 ISTRUZIONI PER L'USO:
echo    1. Copia la cartella 'dist' dove vuoi installare il programma
echo    2. Fai doppio clic su 'GestionaleMagazzinoSpezie.exe'
echo    3. Il browser si aprirà automaticamente con l'applicazione
echo.
echo ⚠️  IMPORTANTE:
echo    - Mantieni sempre il file 'magazzino_data.json' con l'eseguibile
echo    - Fai backup regolari dei tuoi dati
echo    - Il programma deve rimanere in esecuzione per funzionare
echo.
echo 🎯 Compatibilità: Windows 10 e Windows 11
echo 🌐 Accesso: http://localhost:5000
echo.
echo ================================================================
echo.

:: Pulizia ambiente virtuale opzionale
echo Vuoi eliminare l'ambiente virtuale di sviluppo? (consigliato)
echo Questo libererà circa 200MB di spazio ma non influenzerà l'eseguibile.
echo.
set /p CLEANUP="Elimina ambiente virtuale? (S/N): "
if /i "%CLEANUP%"=="S" (
    rmdir /s /q venv
    echo ✅ Ambiente virtuale eliminato
) else (
    echo ℹ️  Ambiente virtuale mantenuto in: %CD%\venv\
)

echo.
echo 🚀 Il tuo Gestionale Magazzino Spezie è pronto all'uso!
echo.
pause