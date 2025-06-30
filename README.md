
# Swahili2Words 🗣️

Convert numeric numbers into Swahili words — including support for decimals, currency, and large numbers (up to billions). You can run the program using command-line arguments or interactively by typing the number when prompted.

---

## ✨ Features

- ✅ Converts numbers like `123` → `mia ishirini na tatu`
- ✅ Handles large numbers: thousands, millions, billions
- ✅ Supports decimal formatting: `123.45` → `mia ishirini na tatu nukta arobaini na tano`
- ✅ Optional currency mode: `--currency` → `shilingi mia ishirini na tatu na senti arobaini na tano`
- ✅ Dual-mode CLI: supports command-line arguments **and** interactive input
- ✅ Lightweight tool — no internet required

---

## 🚀 Installation

First, clone the repo:

```bash
git clone https://github.com/rebreborn/swahili2words.git
cd swahili2words
Then install the package locally:
```
```
pip install .
```
This will install the swahili2words CLI command globally in your Python environment.

🔧 Usage
You can use the CLI in two ways:

🔹 Option 1: Command-Line Arguments
```
python -m swahili2words.cli 1234.56 --currency
```
Output:

```
shilingi elfu moja mia mbili thelathini na nne na senti hamsini na sita
```
🔹 Option 2: Interactive Input
```
python -m swahili2words.cli
```
You'll see:

```
🗣️ Karibu kwenye Swahili2Words!
Ingiza nambari (mfano: 123.45): 1234.56
Ungependa iandikwe kama fedha? (ndiyo/hapana): ndiyo

📝 Matokeo:
shilingi elfu moja mia mbili thelathini na nne na senti hamsini na sita
```

💡 Examples

| Input               | Output                                                  |
| ------------------- | ------------------------------------------------------- |
| `0`                 | sifuri                                                  |
| `15`                | kumi na tano                                            |
| `999`               | mia tisa tisini na tisa                                 |
| `1234`              | elfu moja mia mbili thelathini na nne                   |
| `1000000`           | milioni moja                                            |
| `123.45`            | mia ishirini na tatu nukta arobaini na tano             |
| `123.45` + currency | shilingi mia ishirini na tatu na senti arobaini na tano |


📁 Project Structure
```
swahili2words/
├── swahili2words/
│   ├── __init__.py
│   ├── cli.py
│   └── converter.py
├── setup.py
├── pyproject.toml
└── README.md
```

🛠️ To Do (Suggestions)
 Add support for ordinal numbers (e.g., "wa kwanza", "wa pili")

 Add support for thousands separator parsing (e.g., "1,000")

 Add Swahili ↔ English language toggle

 Add voice output using text-to-speech (--speak)

 Publish to PyPI

🤝 Contributing
Pull requests are welcome! If you'd like to help with grammar, translations, features, or UI, feel free to fork and contribute.

📄 License
MIT License © 2025 Rodrick

🔗 Author
Made with 🇰🇪 & ❤️ by Rodrick Mzaliwa
