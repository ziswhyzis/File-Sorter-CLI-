# 📁 File Sorter CLI

A lightweight, lightning-fast command-line utility to instantly rescue your messy directories. It automatically categorizes and sweeps chaotic files into neatly organized folders based on their extensions[cite: 1].

Built entirely with **pure Python standard libraries**—meaning zero external dependencies and zero setup friction[cite: 1].

---

## ✨ Features
 * **Zero Setup:** No `pip install` required. If you have Python 3, you're ready to go[cite: 1].
 * **Modular Architecture:** Clean separation of configuration, system operations, and CLI interface[cite: 1].
 * **Safe Execution:** Skips existing folders and leaves unknown file extensions completely untouched[cite: 1].
 * **Target Anywhere:** Pass any directory path as a terminal argument to clean it up instantly[cite: 1].

---

## 🛠️ How to Use

### 1. Clone the Repository
Open your terminal and pull down the code[cite: 1]:
```bash
git clone [https://github.com/YOUR_USERNAME/file-sorter-cli.git](https://github.com/YOUR_USERNAME/file-sorter-cli.git)
cd file-sorter-cli
```

### 2. Run the Sorter
Point the script at **any** folder on your computer that needs rescuing[cite: 1]. 

**Example (Cleaning up your Downloads folder):**
```bash
python3 main.py ~/Downloads
```

**Example (Cleaning a specific local project folder):**
```bash
python3 main.py ./path/to/messy_folder
```

---

## ⚙️ Customizing Your Rules
Want to add more file extensions or change folder names? You don't need to touch the core logic. Just open `config.py` and modify the dictionary map[cite: 1]:

```python
EXTENSION_MAP = {
    ".pdf": "PDFs",
    ".txt": "Texts",
    ".mp4": "Videos",
    ".png": "Images",  # Easily add your own mappings here!
}
```
