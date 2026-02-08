# 🚀 PyCompress

**Distribuzione di app Python semplicissima. Due file. Funziona ovunque.**

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#caratteristiche">Caratteristiche</a> •
  <a href="#esempi">Esempi</a> •
  <a href="#documentazione">Documentazione</a> •
  <a href="#contribuire">Contribuire</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/github/stars/rossellamascellani-blip/PyCompress" alt="GitHub Stars">
</p>

> 🇬🇧 **[English Version](README_EN.md)**

---

## Perché PyCompress?

Python è fantastico per lo sviluppo ma **doloroso** per la distribuzione:

```bash
# L'incubo classico:
"Ehi, prova la mia app!"

User: "Come la faccio partire?"
Dev: "Installa Python 3.11, crea venv, pip install -r requirements.txt..."
User: *chiude la tab*
```

**Con PyCompress:**
```bash
"Scarica questi 2 file e lancia: python app.py"
User: "Funziona! 🎉"
```

---

## ✨ Caratteristiche

- **📦 Tool single-file** - Solo `pycompress.py`, nient'altro
- **✅ Controllo versione intelligente** - Avvisa se la versione Python è incompatibile
- **🎯 Packaging zero-config** - Un comando per creare app portabili
- **💾 Persistenza dati** - Le modifiche vengono salvate nel package
- **🐍 Sintassi versione flessibile** - Supporto per `pyv[os]`, `pyv[3.13.1]`, `pyv[>3.11.0]`, `pyv[<3.14.0]`
- **📺 Output pip completo** - Vedi esattamente cosa viene installato
- **🌍 Cross-platform** - Funziona su Windows, macOS e Linux
- **⚡ Estrazione istantanea** - Nessun overhead di compressione (ZIP_STORED)
- **🛡️ Operazioni sicure** - Aggiornamenti atomici prevengono la corruzione dei dati

---

## 🎬 Quick Start

### 1. Impacchetta la tua app

```bash
python pycompress.py my_app/ main.py
```

Questo genera:
- `my_app.pycomp` - La tua applicazione compressa
- `my_app.py` - Script launcher

### 2. Eseguila

```bash
python my_app.py
```

Ecco fatto! Il launcher:
1. ✅ Estrae l'app in una directory temporanea sicura
2. ✅ Controlla la compatibilità della versione Python
3. ✅ Installa le dipendenze con pip
4. ✅ Esegue la tua applicazione
5. ✅ Salva eventuali modifiche nel file `.pycomp`
6. ✅ Pulisce i file temporanei

---

## 📚 Controllo Versione Python

Specifica i requisiti di versione Python nel `requirements.txt`:

```txt
# Accetta qualsiasi versione Python
pyv[os]

# Richiede versione specifica (3.13.x)
pyv[3.13.1]

# Richiede versione minima (>= 3.11.0)
pyv[>3.11.0]

# Richiede versione massima (< 3.14.0)
pyv[<3.14.0]

# Poi elenca le tue dipendenze
requests==2.31.0
numpy>=1.24.0
```

### Gestione Incompatibilità Versione

Se il Python di sistema non corrisponde ai requisiti:

```
═══════════════════════════════════════════════════════
⚠️  INCOMPATIBILITÀ VERSIONE PYTHON
═══════════════════════════════════════════════════════

Richiede Python 3.13.x, hai 3.12.7

Questo programma potrebbe non funzionare correttamente.

Opzioni:
  1. Installa la versione Python corretta
  2. Prova comunque (a tuo rischio)
═══════════════════════════════════════════════════════

Continuare comunque? [s/N]: _
```

L'utente sceglie se procedere. Semplice e pragmatico! ✨

---

## 📦 Dipendenze & Librerie

Metti tutto nel `requirements.txt`:

```txt
# 1. Versione Python (prima riga)
pyv[>3.10.0]

# 2. Le tue librerie
requests==2.31.0
pandas==2.1.4
numpy==1.26.3
beautifulsoup4==4.12.3
```

### Cosa succede quando l'utente esegue la tua app

```bash
python tua_app.py
```

**Output:**
```
[*] Estrazione...
[*] Installazione dipendenze...
============================================================
Collecting requests==2.31.0
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Collecting pandas==2.1.4
  Downloading pandas-2.1.4-cp313-cp313-linux_x86_64.whl
Installing collected packages: requests, pandas, numpy...
Successfully installed requests-2.31.0 pandas-2.1.4 numpy-1.26.3
============================================================
[✓] Dipendenze installate

[*] Esecuzione main.py...
```

Vedi **esattamente** cosa sta facendo pip! Nessun output nascosto.

---

## 💡 Esempi

### Esempio 1: Hello World

**Crea l'app:**
```bash
mkdir hello_app
cd hello_app
```

**main.py:**
```python
print("Ciao da PyCompress!")

# I file persistono tra le esecuzioni!
with open("counter.txt", "a") as f:
    f.write("Esecuzione!\n")
```

**requirements.txt:**
```txt
pyv[os]
```

**Impacchetta ed esegui:**
```bash
cd ..
python pycompress.py hello_app/ main.py
python hello_app.py
```

### Esempio 2: Web Scraper con Dipendenze

**main.py:**
```python
import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quote = soup.find('span', class_='text').text
print(f"Citazione: {quote}")
```

**requirements.txt:**
```txt
pyv[>3.10.0]
requests==2.31.0
beautifulsoup4==4.12.3
```

**Impacchetta ed esegui:**
```bash
python pycompress.py scraper/ main.py
python scraper.py
```

Altri esempi nella directory [`examples/`](examples/)!

---

## 🔧 Come Funziona

### 1. Packaging (`pycompress.py`)

```python
# Crea il file .pycomp (ZIP non compresso)
# Genera il launcher con la logica embedded
```

### 2. Launcher (auto-generato)

Il launcher è uno script Python **auto-contenuto** con:
- Rilevamento OS/versione Python
- Installazione dipendenze
- Esecuzione app
- Sincronizzazione dati

**Nessun file esterno necessario!**

---

## 📖 Documentazione

- **[Guida Quick Start](QUICKSTART.md)** - Inizia in 2 minuti
- **[Guida Sintassi Versione](VERSION_SYNTAX.txt)** - Tutte le opzioni sintassi versione
- **[Demo & Esempi](DEMO.md)** - Tutorial passo-passo
- **[FAQ](FAQ.md)** - Domande comuni
- **[Architettura](ARCHITECTURE.md)** - Come funziona sotto il cofano
- **[Contribuire](CONTRIBUTING.md)** - Unisciti al progetto

---

## 🎯 Casi d'Uso

**Perfetto per:**
- ✅ Demo veloci e prototipi
- ✅ Distribuire tool a utenti non tecnici
- ✅ Tool aziendali interni
- ✅ Progetti educativi
- ✅ Utility CLI
- ✅ Script di elaborazione dati

**Non ideale per:**
- ❌ Applicazioni web di produzione
- ❌ High-performance computing
- ❌ App che richiedono accesso a livello sistema

---

## 🚀 Distribuzione

Condividi la tua app confezionata distribuendo **due file**:

1. `app.pycomp` - L'applicazione impacchettata
2. `app.py` - Il launcher

Gli utenti hanno solo bisogno di Python installato. Tutto qui!

---

## 🛠️ Roadmap

- [x] Packaging base
- [x] Persistenza dati
- [x] Controllo versione Python con sintassi flessibile
- [x] Visibilità completa output pip
- [ ] Verifica integrità SHA256
- [ ] Opzioni di compressione (ZIP_DEFLATED)
- [ ] Firme digitali
- [ ] GUI per non-sviluppatori

---

## 🤝 Contribuire

Amiamo i contributi! Vedi [CONTRIBUTING.md](CONTRIBUTING.md) per le linee guida.

**Modi per contribuire:**
- 🐛 Segnala bug
- 💡 Suggerisci funzionalità
- 📝 Migliora la documentazione
- 🔧 Invia pull request
- ⭐ Metti una stella al repo!

---

## 📄 Licenza

Licenza MIT - vedi [LICENSE](LICENSE) per i dettagli.

---

## 🙏 Riconoscimenti

Ispirato da:
- File JAR (Java)
- AppImage (Linux)
- Portable Apps
- La frustrazione collettiva con il packaging Python 😅

---

## 💬 Community

- **Issues**: [GitHub Issues](https://github.com/rossellamascellani-blip/PyCompress/issues)
- **Discussioni**: [GitHub Discussions](https://github.com/rossellamascellani-blip/PyCompress/discussions)

---

<p align="center">
  <b>Costruito con frustrazione e determinazione</b> 🔥<br>
  Smetti di combattere con pip, venv e PyInstaller. Comprimi ed esegui.
</p>

<p align="center">
  Fatto con ❤️ da <a href="https://github.com/rossellamascellani-blip">rossellamascellani-blip</a>
</p>
