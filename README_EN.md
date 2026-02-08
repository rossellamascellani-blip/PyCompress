# 🚀 PyCompress

**Dead-simple Python app distribution. Two files. Works everywhere.**

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#features">Features</a> •
  <a href="#examples">Examples</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/github/stars/rossellamascellani-blip/PyCompress" alt="GitHub Stars">
</p>

> 🇮🇹 **[Versione Italiana](README_IT.md)**

---

## Why PyCompress?

Python is amazing for development but **painful** for distribution:

```bash
# The usual nightmare:
"Hey, try my app!"

User: "How do I run it?"
Dev: "Install Python 3.11, create venv, pip install -r requirements.txt..."
User: *closes tab*
```

**With PyCompress:**
```bash
"Download these 2 files and run: python app.py"
User: "It works! 🎉"
```

---

## ✨ Features

- **📦 Single-file tool** - Just `pycompress.py`, nothing else needed
- **✅ Smart version checking** - Warns if Python version is incompatible
- **🎯 Zero-config packaging** - One command to create portable apps
- **💾 Data persistence** - Changes are saved back to the package
- **🐍 Flexible version syntax** - Support for `pyv[os]`, `pyv[3.13.1]`, `pyv[>3.11.0]`, `pyv[<3.14.0]`
- **📺 Full pip output** - See exactly what's being installed
- **🌍 Cross-platform** - Works on Windows, macOS, and Linux
- **⚡ Instant extraction** - No compression overhead (ZIP_STORED)
- **🛡️ Safe operations** - Atomic updates prevent data corruption

---

## 🎬 Quick Start

### 1. Package your app

```bash
python pycompress.py my_app/ main.py
```

This generates:
- `my_app.pycomp` - Your compressed application
- `my_app.py` - Launcher script

### 2. Run it

```bash
python my_app.py
```

That's it! The launcher will:
1. ✅ Extract the app to a secure temp directory
2. ✅ Check Python version compatibility
3. ✅ Install dependencies with pip
4. ✅ Run your application
5. ✅ Save any changes back to the `.pycomp` file
6. ✅ Clean up temp files

---

## 📚 Python Version Control

Specify Python version requirements in `requirements.txt`:

```txt
# Accept any Python version
pyv[os]

# Require specific version (3.13.x)
pyv[3.13.1]

# Require minimum version (>= 3.11.0)
pyv[>3.11.0]

# Require maximum version (< 3.14.0)
pyv[<3.14.0]

# Then list your dependencies
requests==2.31.0
numpy>=1.24.0
```

### Version Mismatch Handling

If the system's Python doesn't match requirements:

```
═══════════════════════════════════════════════════════
⚠️  PYTHON VERSION INCOMPATIBILITY
═══════════════════════════════════════════════════════

Requires Python 3.13.x, you have 3.12.7

This program may not work correctly.

Options:
  1. Install the correct Python version
  2. Try anyway (at your own risk)
═══════════════════════════════════════════════════════

Continue anyway? [y/N]: _
```

User chooses whether to proceed. Simple and pragmatic! ✨

---

## 📦 Dependencies & Libraries

Put everything in `requirements.txt`:

```txt
# 1. Python version (first line)
pyv[>3.10.0]

# 2. Your libraries
requests==2.31.0
pandas==2.1.4
numpy==1.26.3
beautifulsoup4==4.12.3
```

### What happens when user runs your app

```bash
python your_app.py
```

**Output:**
```
[*] Extraction...
[*] Installing dependencies...
============================================================
Collecting requests==2.31.0
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Collecting pandas==2.1.4
  Downloading pandas-2.1.4-cp313-cp313-linux_x86_64.whl
Installing collected packages: requests, pandas, numpy...
Successfully installed requests-2.31.0 pandas-2.1.4 numpy-1.26.3
============================================================
[✓] Dependencies installed

[*] Executing main.py...
```

You see **exactly** what pip is doing! No hidden output.

---

## 💡 Examples

### Example 1: Hello World

**Create the app:**
```bash
mkdir hello_app
cd hello_app
```

**main.py:**
```python
print("Hello from PyCompress!")

# Files persist between runs!
with open("counter.txt", "a") as f:
    f.write("Run!\n")
```

**requirements.txt:**
```txt
pyv[os]
```

**Package and run:**
```bash
cd ..
python pycompress.py hello_app/ main.py
python hello_app.py
```

### Example 2: Web Scraper with Dependencies

**main.py:**
```python
import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quote = soup.find('span', class_='text').text
print(f"Quote: {quote}")
```

**requirements.txt:**
```txt
pyv[>3.10.0]
requests==2.31.0
beautifulsoup4==4.12.3
```

**Package and run:**
```bash
python pycompress.py scraper/ main.py
python scraper.py
```

More examples in the [`examples/`](examples/) directory!

---

## 🔧 How It Works

### 1. Packaging (`pycompress.py`)

```python
# Creates .pycomp file (uncompressed ZIP)
# Generates launcher with embedded logic
```

### 2. Launcher (auto-generated)

The launcher is a **self-contained** Python script with:
- OS/Python version detection
- Dependency installation
- App execution
- Data synchronization

**No external files needed!**

---

## 📖 Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get started in 2 minutes
- **[Version Syntax Guide](VERSION_SYNTAX.txt)** - All version syntax options
- **[Demo & Examples](DEMO.md)** - Step-by-step tutorials
- **[FAQ](FAQ.md)** - Common questions answered
- **[Architecture](ARCHITECTURE.md)** - How it works under the hood
- **[Contributing](CONTRIBUTING.md)** - Join the project

---

## 🎯 Use Cases

**Perfect for:**
- ✅ Quick demos and prototypes
- ✅ Distributing tools to non-technical users
- ✅ Internal company tools
- ✅ Educational projects
- ✅ CLI utilities
- ✅ Data processing scripts

**Not ideal for:**
- ❌ Production web applications
- ❌ High-performance computing
- ❌ Apps requiring system-level access

---

## 🚀 Distribution

Share your packaged app by distributing **two files**:

1. `app.pycomp` - The packaged application
2. `app.py` - The launcher

Users just need Python installed. That's it!

---

## 🛠️ Roadmap

- [x] Basic packaging
- [x] Data persistence
- [x] Python version checking with flexible syntax
- [x] Full pip output visibility
- [ ] SHA256 integrity verification
- [ ] Compression options (ZIP_DEFLATED)
- [ ] Digital signatures
- [ ] GUI for non-developers

---

## 🤝 Contributing

We love contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests
- ⭐ Star the repo!

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Inspired by:
- JAR files (Java)
- AppImage (Linux)
- Portable Apps
- The collective frustration with Python packaging 😅

---

## 💬 Community

- **Issues**: [GitHub Issues](https://github.com/rossellamascellani-blip/PyCompress/issues)
- **Discussions**: [GitHub Discussions](https://github.com/rossellamascellani-blip/PyCompress/discussions)

---

<p align="center">
  <b>Built with frustration and determination</b> 🔥<br>
  Stop fighting with pip, venv, and PyInstaller. Just compress and run.
</p>

<p align="center">
  Made with ❤️ by <a href="https://github.com/rossellamascellani-blip">rossellamascellani-blip</a>
</p>
