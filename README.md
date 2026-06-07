# 📁 File Sorter CLI

A lightweight, lightning-fast command-line utility to instantly rescue your messy directories. It automatically categorizes and sweeps chaotic files into neatly organized folders based on their extensions.

Built entirely with **pure Python standard libraries**—meaning zero external dependencies and zero setup friction across Windows, macOS, and Linux.

---

## ✨ Features
* **Zero Setup:** No `pip install` required. If you have Python 3, you're ready to go.
* **Modular Design:** Clean, simple separation of sorting rules and core code.
* **Safe Execution:** Skips existing folders and leaves unknown file types completely untouched.
* **Target Anywhere:** Pass any directory path as a terminal argument to clean it up instantly.

---

## 🐍 Don't have Python?
This tool requires **Python 3**. You can check if you already have it by typing `python --version` or `python3 --version` in your terminal. 

If you need to install it:
* **Windows:** Download it directly from the official **Microsoft Store** app (search for "Python") or [python.org](https://www.python.org/downloads/).
* **Linux (Ubuntu):** Open your terminal and run `sudo apt install python3`.
* **macOS:** Open your terminal and run `brew install python` or download it from [python.org](https://www.python.org/downloads/).

---

## 🛠️ How to Use

### 1. Clone the Repository
Open your terminal (or Command Prompt/PowerShell on Windows) and run:
```bash
git clone https://github.com/ziswhyzis/File-Sorter-CLI-.git
cd File-Sorter-CLI-
```

### 2. Run the Sorter
Point the script at **any** folder on your computer that needs rescuing. 

#### 💻 On Windows
Use `python` and specify your folder path like this:
```cmd
python main.py C:\Users\YourName\Downloads
```
*(Tip: You can copy-paste your exact folder path straight from the Windows File Explorer address bar!)*

#### 🐧 On Linux / macOS
Use `python3` and specify your folder path like this:
```bash
python3 main.py ~/Downloads
```

---

## ⚙️ Customizing Your Rules
Want to add more file extensions or change folder names? You don't need to touch the core code. Just open `config.py` in any text editor and edit the dictionary map:

```python
EXTENSION_MAP = {
    ".pdf": "PDFs",
    ".txt": "Texts",
    ".mp4": "Videos",
    ".png": "Images",  # Add your own custom rules here!
}
```