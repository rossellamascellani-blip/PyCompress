import zipfile
import os
import sys

def pycompress(target_folder, main_file):
    folder_name = os.path.basename(os.path.normpath(target_folder))
    zip_name = f"{folder_name}.pycomp"
    runner_name = f"{folder_name}.py"

    # Creazione iniziale dello ZIP
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_STORED) as zipf:
        for root, dirs, files in os.walk(target_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, target_folder)
                zipf.write(file_path, arcname)
    
    # Launcher con VERSION CHECK (non download!)
    runner_content = f"""import zipfile
import os
import subprocess
import sys
import shutil
import tempfile
import platform
import re

zip_file = "{zip_name}"
main_script = "{main_file}"

def parse_python_version(req_file):
    \"\"\"Legge versione Python da requirements.txt (pyv[...])\"\"\"
    if not os.path.exists(req_file):
        return None
    with open(req_file, 'r') as f:
        for line in f:
            line = line.strip()
            match = re.match(r'pyv\\[([^\\]]+)\\]', line)
            if match:
                return match.group(1)
    return None

def parse_version_tuple(version_str):
    \"\"\"Converte '3.13.1' in (3, 13, 1)\"\"\"
    parts = version_str.split('.')
    return tuple(int(p) for p in parts if p.isdigit())

def check_python_version(requirement):
    \"\"\"Verifica se Python di sistema soddisfa i requisiti\"\"\"
    if requirement == "os":
        return True, None  # pyv[os] = accetta qualsiasi versione
    
    current = sys.version_info
    current_str = f"{{current.major}}.{{current.minor}}.{{current.micro}}"
    
    # pyv[<3.13.5] = versione deve essere < 3.13.5
    if requirement.startswith('<'):
        required_ver = parse_version_tuple(requirement[1:])
        if current[:len(required_ver)] < required_ver:
            return True, None
        else:
            return False, f"Richiede Python < {{requirement[1:]}}, hai {{current_str}}"
    
    # pyv[>3.13.5] = versione deve essere >= 3.13.5
    elif requirement.startswith('>'):
        required_ver = parse_version_tuple(requirement[1:])
        if current[:len(required_ver)] >= required_ver:
            return True, None
        else:
            return False, f"Richiede Python >= {{requirement[1:]}}, hai {{current_str}}"
    
    # pyv[3.13.1] = versione esatta (match su major.minor)
    else:
        required_ver = parse_version_tuple(requirement)
        # Match su major.minor, tollerante su micro
        if len(required_ver) >= 2:
            if current.major == required_ver[0] and current.minor == required_ver[1]:
                return True, None
            else:
                return False, f"Richiede Python {{required_ver[0]}}.{{required_ver[1]}}.x, hai {{current_str}}"
        else:
            return True, None

def save_changes_back(extract_dir):
    \"\"\"Salva modifiche nello ZIP (atomic)\"\"\"
    print(f"[*] Salvataggio modifiche...")
    temp_zip = zip_file + ".tmp"
    with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_STORED) as zipf:
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, extract_dir)
                zipf.write(file_path, arcname)
    os.replace(temp_zip, zip_file)

def install_deps(extract_dir):
    \"\"\"Installa dipendenze con pip (mostra output)\"\"\"
    req_file = os.path.join(extract_dir, "requirements.txt")
    if not os.path.exists(req_file):
        return
    
    print("[*] Installazione dipendenze...")
    print("=" * 60)
    
    # Usa --user per installare senza permessi root se necessario
    cmd = [sys.executable, "-m", "pip", "install", "-r", req_file]
    
    # Su Linux potrebbe servire --break-system-packages
    if platform.system() != "Windows":
        cmd.append("--break-system-packages")
    
    try:
        subprocess.check_call(cmd)
        print("=" * 60)
        print("[✓] Dipendenze installate")
    except subprocess.CalledProcessError:
        print("=" * 60)
        print("[!] ATTENZIONE: Alcune dipendenze potrebbero non essere installate")

def main():
    if not os.path.exists(zip_file):
        print(f"[!] Errore: {{zip_file}} non trovato")
        sys.exit(1)
    
    extract_dir = tempfile.mkdtemp(prefix="pycomp_")
    
    try:
        # Estrazione
        print(f"[*] Estrazione...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        # Legge e verifica versione Python
        req_file = os.path.join(extract_dir, "requirements.txt")
        python_requirement = parse_python_version(req_file)
        
        if python_requirement and python_requirement != "os":
            compatible, error_msg = check_python_version(python_requirement)
            
            if not compatible:
                print("=" * 60)
                print("⚠️  INCOMPATIBILITÀ VERSIONE PYTHON")
                print("=" * 60)
                print(f"\\n{{error_msg}}\\n")
                print("Questo programma potrebbe non funzionare correttamente.")
                print("\\nOpzioni:")
                print("  1. Installa la versione Python corretta")
                print("  2. Prova comunque (a tuo rischio)")
                print("=" * 60)
                
                choice = input("\\nContinuare comunque? [s/N]: ").lower()
                if choice != 's':
                    print("[*] Esecuzione annullata")
                    return
                print()
        
        # Installa dipendenze (senza venv!)
        install_deps(extract_dir)
        
        # RUN!
        print(f"\\n[*] Esecuzione {{main_script}}...")
        print("=" * 60)
        original_cwd = os.getcwd()
        os.chdir(extract_dir)
        result = subprocess.run([sys.executable, main_script])
        os.chdir(original_cwd)
        print("=" * 60)
        
    finally:
        # Salva e cleanup
        save_changes_back(extract_dir)
        print("[*] Cleanup...")
        shutil.rmtree(extract_dir, ignore_errors=True)
        print("[✓] Done!")

if __name__ == "__main__":
    main()
"""
    
    with open(runner_name, "w", encoding="utf-8") as f:
        f.write(runner_content.strip())

    print(f"✓ Creati: {zip_name} e {runner_name}")
    print(f"✓ Launcher con version check integrato!")
    print(f"\nSintassi requirements.txt:")
    print(f"  pyv[os]      → Accetta qualsiasi versione")
    print(f"  pyv[3.13.1]  → Richiede Python 3.13.x")
    print(f"  pyv[>3.11.0] → Richiede Python >= 3.11.0")
    print(f"  pyv[<3.14.0] → Richiede Python < 3.14.0")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Utilizzo: python pycompress.py <cartella_target> <file_main.py>")
    else:
        pycompress(sys.argv[1], sys.argv[2])
