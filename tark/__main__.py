import sys

# Hindi to Python keyword mapping
HINDI_TO_PYTHON = {
    "likho": "print",          # print function
    "agar": "if",              # if statement
    "warna": "else",           # else statement
    "jabtak": "while",         # while loop
    "ke_liye": "for",          # for loop
    "sach": "True",            # boolean True
    "jhooth": "False",         # boolean False
    "kaam": "def",             # function definition
    "wapas": "return",         # return from function
    "ruk_jao": "break",        # break loop
    "aage_badh": "continue",   # continue loop
    "nahi": "not",             # logical not
    "aur": "and",              # logical and
    "ya": "or",                # logical or
}

def transpile(code):
    lines = code.splitlines()
    final_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") or stripped.startswith("//"):
            continue  # skip comment lines

        # Replace Hindi keywords with Python equivalents
        for hindi, eng in HINDI_TO_PYTHON.items():
            line = line.replace(hindi, eng)

        final_lines.append(line)

    return "\n".join(final_lines)

def main():
    if len(sys.argv) != 2:
        print("❗ उपयोग: tark <file.tk>")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
            python_code = transpile(code)
            exec(python_code)
    except FileNotFoundError:
        print(f"❌ फ़ाइल नहीं मिली: {file_path}")
    except Exception as e:
        print("⚠️ त्रुटि:", e)
