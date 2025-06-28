
# Tark — A Hindi Programming Language | एक हिंदी प्रोग्रामिंग भाषा

> Tark (तर्क) means *"logic"* in Hindi.  
> It is a beginner-friendly, open-source programming language that allows you to write code in **Hindi syntax**.


## What is Tark?

**Tark** is an experimental, interpreted language designed to make programming more accessible to native Hindi speakers — especially school students, rural learners, and first-time coders.

Tark is written in Python and transpiles Hindi code into Python, then runs it instantly.


## Features

- Write code using Hindi keywords like `agar`, `likho`, `warna`
- Runs on Linux, macOS, and Windows
- Installable like Python (`tark file.tk`)
- Open-source and developer friendly



## 💻 हिंदी में कोड कैसे लिखें? (How to Code in Hindi)

```hindi
sankhya = 10

agar sankhya > 5:
    likho("Ye sankhya 5 se badi hai")
warna:
    likho("Ye sankhya 5 ya usse chhoti hai")
````

Save this in a file like `src/app.tk` and run it with Tark.



## 🛠️ Installation (for Users)

### 1. System Requirements

* Python 3.6 or above
* Git installed


### 2. Install Tark via Git (Editable Mode)

```bash
git clone https://github.com/BitCraftProduction/tark.git
cd tark
pip install -e .
```

Now Tark is installed system-wide. You can run:

```bash
tark src/app.tk
```



### 3. File Naming Convention

* Use `.tk` as the file extension for Tark source files.
* Recommended structure:

  ```
  tark/
  ├── src/
  │   └── app.tk
  ```


## 🤝 Contribution Guide (for Developers)

Want to help grow Tark? Follow these steps:

### 1. Fork and Clone

```bash
git clone https://github.com/your-username/tark.git
cd tark
```

### 2. Structure

```
tark/
├── tark/              ← Python package
│   ├── __main__.py    ← CLI entry point
│   └── __init__.py
├── setup.py           ← Packaging config
├── pyproject.toml     ← Build metadata
├── src/app.tk         ← Sample Tark code
└── README.md
```

### 3. Install in Dev Mode

```bash
pip install -e .
```

Now you can test Tark anywhere using:

```bash
tark src/app.tk
```



## Planned Features (Coming Soon)

* `tark repl` interactive terminal
* `tark web` – online web IDE
* Hindi error messages
* Variable and function renaming in Hindi
* `.deb`, `.exe`, and `pip` installer
* Syntax highlighter + VS Code extension



## 🌐 Keywords Mapping

| Hindi    | Python |
| -------- | ------ |
| likho    | print  |
| agar     | if     |
| warna    | else   |
| jabtak   | while  |
| ke\_liye | for    |
| sach     | True   |
| jhooth   | False  |



## 📄 License

This project is licensed under the [MIT License](./LICENSE).
Free to use, modify, and share with proper credit.


## ✨ Made in India with ❤️

By [BitCraft Production & Developers](https://www.bitcraftproduction.com)
Join the mission to make programming accessible to every Indian.

🇮🇳 *"Code Bharat Mein, Bharat Ki Bhasha Mein."*

