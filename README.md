# 🔐 Password Strength Analyzer & Wordlist Generator

A dual-purpose security tool for:

- **Analyzing password strength**
- **Generating targeted password wordlists**

This tool is useful for red teamers, penetration testers, or anyone who wants to test password resilience or create realistic wordlists for audit.

---

## 📦 Features

### 🔍 Password Analyzer
- Uses [`zxcvbn`](https://github.com/dropbox/zxcvbn) to assess password strength
- Crack time estimation & feedback
- Password preview toggle (GUI)

### 🧠 Custom Wordlist Generator
- Inputs: name, birth date, pet name, favorite book, car/bike, etc.
- Adds leetspeak, case flips, year suffixes, common patterns
- Outputs `.txt` files under `wordlists/` folder
- File auto-naming with timestamp + unique ID
- Prompts for overwrite & auto-opens file (GUI)

### 🖼️ GUI with Tkinter
- Tabs for password analysis and wordlist generation
- Toggle to show/hide password input
- User-friendly experience

---

## 🚀 Getting Started

### 🧰 Requirements

Create virtual environment:
```bash
venv\Scripts\activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```

### ▶️ Run (CLI)
```bash
python main.py
```
### 🖱️ Run (GUI)
```bash
python app/gui_main.py
```

### 📁 Project Structure
```bash
password_strength_analyzer/
├── app/
│   ├── analyzer.py
│   ├── generator.py
│   ├── ui_cli.py
│   └── gui_main.py
├── wordlists/
├── main.py
├── requirements.txt
```

### 🧾 License
MIT License © 2025 Pradeep Behera
```bash
Feel free to download.
```
