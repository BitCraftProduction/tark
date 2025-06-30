
## 📘 Tark Programming Language – Syntax & Documentation

> *A Hindi-first programming language for Bharat coders.*


### उद्देश्य | Purpose

**Tark** (तर्क) is a beginner-friendly programming language written in Hindi, designed to make coding more natural and logical for Hindi-speaking learners. Tark code is transpiled to Python and runs instantly.



## 📄 फ़ाइल एक्सटेंशन | File Extension

All Tark programs use:

```
.tk
```

Example:

```bash
tark src/app.tk
```



## बेसिक सिंटैक्स | Basic Syntax

| हिंदी कीवर्ड (Tark) | English Equivalent | उपयोग / Use                         |
| ------------------- | ------------------ | ----------------------------------- |
| `likho`             | `print`            | Output दिखाने के लिए                |
| `agar`              | `if`               | Condition जाँचने के लिए             |
| `warna`             | `else`             | वैकल्पिक स्थिति के लिए              |
| `jabtak`            | `while`            | Loop चलाने के लिए                   |
| `ke_liye`           | `for`              | Repeat करने के लिए                  |
| `sach`              | `True`             | True वैल्यू                         |
| `jhooth`            | `False`            | False वैल्यू                        |
| `kaam`              | `def`              | Function बनाने के लिए               |
| `wapas`             | `return`           | Function से वैल्यू वापस देने के लिए |
| `ruk_jao`           | `break`            | Loop से बाहर निकलने के लिए          |
| `aage_badh`         | `continue`         | Loop की अगली iteration के लिए       |
| `nahi`              | `not`              | Logical NOT                         |
| `aur`               | `and`              | Logical AND                         |
| `ya`                | `or`               | Logical OR                          |



## Example Tark Code (with Explanation)

```hindi
# यह एक Tark प्रोग्राम है

kaam abhinandan(naam):
    likho("Namaste, " + naam)   # greet the user

abhinandan("Ganesh")            # function call

ganana = 0

jabtak ganana < 5:              # while loop
    ganana = ganana + 1

    agar ganana == 3:           # if condition
        aage_badh               # continue loop

    agar ganana == 4:
        ruk_jao                 # break loop

    likho("Ganati: " + str(ganana))
```



## Comments in Tark

Use `#` or `//` to write comments. Tark will ignore them.

```hindi
# यह टिप्पणी है
// यह भी टिप्पणी है
likho("Hello")  # यह भी काम करता है
```



## 📁 Recommended Project Structure

```
tark/
├── docs/              ← Tark Syntax Docs
├── tark/              ← Python package
│   ├── __main__.py    ← CLI entry point
│   └── __init__.py
├── setup.py           ← Packaging config
├── pyproject.toml     ← Build metadata
├── src/app.tk         ← Sample Tark code
└── README.md
```



## चलाने की विधि | How to Run Tark Code

### 1. एक `.tk` फ़ाइल बनाएँ (Write `.tk` file):

```hindi
likho("Tark v0.2 me aapka swagat hai!")
```

### 2. टर्मिनल में चलाएँ (Run in terminal):

```bash
tark src/app.tk
```

You must have Tark installed (`pip install -e .`)


## योजनाएं (Upcoming Features)

* `tark repl` – interactive shell
* `tark --version`, `--help`
* Variable renaming (in Hindi)
* Hindi error messages
* Web playground
* `.deb` & `.exe` installer

