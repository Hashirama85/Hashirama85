@echo off
title Gestionale Magazzino Spezie - Creazione Eseguibile Windows
color 0A

echo.
echo ========================================
echo   GESTIONALE MAGAZZINO SPEZIE
echo   Creazione Eseguibile per Windows
echo ========================================
echo.

echo Verifica Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRORE: Python non trovato. Installa Python 3.8 o superiore.
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Python trovato
echo.

echo Installazione/Aggiornamento dipendenze...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Avvio creazione eseguibile...
echo Questo processo potrebbe richiedere alcuni minuti...
echo.

python build_exe.py

echo.
echo Processo completato!
pause