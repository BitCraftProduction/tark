import sys

HINDI_TO_PYTHON = {
    "likho": "print",
    "agar": "if",
    "warna": "else",
    "jabtak": "while",
    "ke_liye": "for",
    "sach": "True",
    "jhooth": "False"
}

def transpile(code):
    for hindi, eng in HINDI_TO_PYTHON.items():
        code = code.replace(hindi, eng)
    return code

def main():
    if len(sys.argv) != 2:
        print("उपयोग: tark <file.tk>")
        return

    file_path = sys.argv[1]
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    python_code = transpile(code)
    exec(python_code)
