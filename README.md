# Swahili2Words 🗣️

Convert numeric numbers into Swahili words — including support for decimals, currency, and large numbers (up to billions).

---

## ✨ Features

- ✅ Converts numbers like `123` → `mia ishirini na tatu`
- ✅ Handles large numbers: thousands, millions, billions
- ✅ Supports decimal formatting: `123.45` → `mia ishirini na tatu nukta arobaini na tano`
- ✅ Optional currency mode: `--currency` → `shilingi mia ishirini na tatu na senti arobaini na tano`
- ✅ Lightweight CLI tool — no internet needed

---

## 🚀 Installation

First, clone the repo:

```bash
git clone https://github.com/rebreborn/swahili2words.git
cd swahili2words
Install locally using pip:

bash

pip install .
This will install the swahili2words command globally in your Python environment.

🔧 Usage
bash

swahili2words 123456.78
Output:

nginx

laki moja ishirini na tatu elfu mia nne hamsini na sita nukta sabini na nane
🪙 Currency Mode
bash

swahili2words 123456.78 --currency
Output:

nginx

shilingi laki moja ishirini na tatu elfu mia nne hamsini na sita na senti sabini na nane
💡 Examples
Input	Command	Output
0	swahili2words 0	sifuri
15	swahili2words 15	kumi na tano
999	swahili2words 999	mia tisa tisini na tisa
1234	swahili2words 1234	elfu moja mia mbili thelathini na nne
1000000	swahili2words 1000000	milioni moja
123.45	swahili2words 123.45 --currency	shilingi mia ishirini na tatu na senti arobaini na tano

📁 Project Structure
arduino

swahili2words/
├── swahili2words/
│   ├── __init__.py
│   ├── cli.py
│   └── converter.py
├── setup.py
├── pyproject.toml
└── README.md
🛠️ To Do (Suggestions)
Add support for ordinal numbers (e.g., "wa kwanza", "wa pili")

Add support for thousands separator parsing (e.g., "1,000")

Add Swahili ↔ English toggle

Publish to PyPI

🤝 Contributing
Pull requests are welcome! If you'd like to help with grammar, new languages, or more features, feel free to fork and improve the tool.

📄 License
MIT License © 2025 Rodrick

🔗 Author
Made with 🇰🇪 & ❤️ by Rodrick
