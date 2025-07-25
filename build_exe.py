"""
Script per creare l'eseguibile Windows del Gestionale Magazzino Spezie
Compatibile con Windows 10 e 11
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_executable():
    """Crea l'eseguibile Windows usando PyInstaller"""
    
    print("🔧 Creazione eseguibile Gestionale Magazzino Spezie per Windows...")
    print("=" * 60)
    
    # Verifica che PyInstaller sia installato
    try:
        import PyInstaller
        print(f"✅ PyInstaller versione {PyInstaller.__version__} trovato")
    except ImportError:
        print("❌ PyInstaller non trovato. Installazione in corso...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller==6.3.0"])
        print("✅ PyInstaller installato correttamente")
    
    # Verifica che Flask sia installato
    try:
        import flask
        print(f"✅ Flask versione {flask.__version__} trovato")
    except ImportError:
        print("❌ Flask non trovato. Installazione dipendenze...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dipendenze installate correttamente")
    
    # Directory di output
    dist_dir = Path("dist")
    build_dir = Path("build")
    
    # Pulisci directory precedenti
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
        print("🗑️  Directory dist precedente rimossa")
    
    if build_dir.exists():
        shutil.rmtree(build_dir)
        print("🗑️  Directory build precedente rimossa")
    
    # Crea il file spec per PyInstaller
    spec_content = """
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('static', 'static'),
    ],
    hiddenimports=[
        'flask',
        'werkzeug',
        'jinja2',
        'markupsafe',
        'itsdangerous',
        'click',
        'blinker',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GestionaleMagazzinoSpezie',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    version='version_info.txt'
)
"""
    
    # Crea il file version_info.txt per informazioni sulla versione
    version_info = """
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1,0,0,0),
    prodvers=(1,0,0,0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Gestionale Magazzino'),
        StringStruct(u'FileDescription', u'Gestionale per Magazzino Spezie e Ingredienti'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'GestionaleMagazzinoSpezie'),
        StringStruct(u'LegalCopyright', u'Copyright 2024'),
        StringStruct(u'OriginalFilename', u'GestionaleMagazzinoSpezie.exe'),
        StringStruct(u'ProductName', u'Gestionale Magazzino Spezie'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""
    
    # Salva i file
    with open("app.spec", "w", encoding="utf-8") as f:
        f.write(spec_content)
    
    with open("version_info.txt", "w", encoding="utf-8") as f:
        f.write(version_info)
    
    print("📝 File di configurazione PyInstaller creati")
    
    try:
        # Esegui PyInstaller
        print("\n🚀 Avvio creazione eseguibile...")
        result = subprocess.run([
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--noconfirm",
            "app.spec"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Eseguibile creato con successo!")
            
            # Verifica che l'eseguibile sia stato creato
            exe_path = dist_dir / "GestionaleMagazzinoSpezie.exe"
            if exe_path.exists():
                size_mb = exe_path.stat().st_size / (1024 * 1024)
                print(f"📦 File eseguibile: {exe_path}")
                print(f"📏 Dimensione: {size_mb:.1f} MB")
                
                # Crea un README per l'utente
                readme_content = """
# Gestionale Magazzino Spezie - Guida all'uso

## Come avviare il programma

1. Fai doppio clic su 'GestionaleMagazzinoSpezie.exe'
2. Attendi che si apra il browser automaticamente
3. Se il browser non si apre, vai manualmente su: http://localhost:5000

## Funzionalità principali

- ✅ Gestione prodotti (spezie/ingredienti)
- ✅ Carico e scarico con lotti
- ✅ Tracciabilità completa
- ✅ Controllo scadenze
- ✅ Storico movimenti
- ✅ Principio FIFO (First In, First Out)

## Caratteristiche

- Interface web moderna e responsive
- Dati salvati localmente nel file 'magazzino_data.json'
- Compatibile con Windows 10 e 11
- Non richiede connessione internet (dopo il primo avvio)

## Requisiti di sistema

- Windows 10 (versione 1903 o superiore)
- Windows 11 (tutte le versioni)
- 4 GB di RAM minimo
- 100 MB di spazio libero su disco

## Supporto

Per problemi o suggerimenti, conserva questo file README
insieme all'eseguibile per riferimenti futuri.

## Backup dei dati

IMPORTANTE: Il file 'magazzino_data.json' contiene tutti i tuoi dati.
Fai backup regolari di questo file per non perdere le informazioni.

Versione: 1.0.0
Data build: 2024
"""
                
                with open(dist_dir / "README.txt", "w", encoding="utf-8") as f:
                    f.write(readme_content)
                
                print("📚 README.txt creato")
                
                print("\n" + "="*60)
                print("🎉 ESEGUIBILE CREATO CON SUCCESSO!")
                print("="*60)
                print(f"📂 Cartella: {dist_dir.absolute()}")
                print("📋 File inclusi:")
                print("   - GestionaleMagazzinoSpezie.exe (applicazione principale)")
                print("   - README.txt (guida all'uso)")
                print("\n💡 ISTRUZIONI:")
                print("1. Copia la cartella 'dist' dove vuoi installare il programma")
                print("2. Fai doppio clic su GestionaleMagazzinoSpezie.exe per avviare")
                print("3. Il browser si aprirà automaticamente")
                print("\n⚠️  IMPORTANTE:")
                print("- Tieni sempre il file 'magazzino_data.json' insieme all'eseguibile")
                print("- Fai backup regolari del file dati")
                print("- Il programma deve rimanere in esecuzione per funzionare")
                
            else:
                print("❌ Errore: Eseguibile non trovato dopo la compilazione")
                return False
                
        else:
            print("❌ Errore durante la creazione dell'eseguibile:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")
        return False
    
    finally:
        # Pulisci file temporanei
        for temp_file in ["app.spec", "version_info.txt"]:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        
        if build_dir.exists():
            shutil.rmtree(build_dir)
    
    return True

def main():
    """Funzione principale"""
    print("🏭 Gestionale Magazzino Spezie - Generatore Eseguibile Windows")
    print("Compatibile con Windows 10 e Windows 11")
    print()
    
    # Verifica che siamo nella directory corretta
    if not os.path.exists("app.py"):
        print("❌ Errore: app.py non trovato nella directory corrente")
        print("Assicurati di essere nella directory del progetto")
        return
    
    if not os.path.exists("templates"):
        print("❌ Errore: directory 'templates' non trovata")
        print("Assicurati di essere nella directory del progetto")
        return
    
    # Avvia la creazione
    success = create_executable()
    
    if success:
        print("\n✨ Processo completato con successo!")
        input("\nPremi INVIO per chiudere...")
    else:
        print("\n💥 Processo fallito. Controlla gli errori sopra.")
        input("\nPremi INVIO per chiudere...")

if __name__ == "__main__":
    main()