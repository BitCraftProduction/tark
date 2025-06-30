import sys
import traceback

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

# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def transpile(code):
    lines = code.splitlines()
    final_lines = []

    for i, line in enumerate(lines):
        original_line = line  # For error context
        stripped = line.strip()

        # Skip full-line comments
        if stripped.startswith("#") or stripped.startswith("//"):
            continue

        # Handle inline comments
        if "#" in line:
            code_part, comment_part = line.split("#", 1)
            line = code_part.strip()  # Ignore comment
        else:
            comment_part = ""

        # Replace Hindi keywords with Python
        for hindi, eng in HINDI_TO_PYTHON.items():
            # Replace only whole words, not substrings
            line = line.replace(f"{hindi}", f"{eng}")

        # Reconstruct with indentation
        indent = " " * (len(original_line) - len(original_line.lstrip()))
        final_lines.append(indent + line)

    return "\n".join(final_lines)

def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("--help", "-h"):
        print(f"""
{CYAN}📘 Tark - एक हिंदी प्रोग्रामिंग भाषा
{RESET}उपयोग: tark <file.tk>

उदाहरण:
  tark src/mera_program.tk
        """)
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
            python_code = transpile(code)

            print(f"{GREEN}🔧 Executing {file_path}...{RESET}\n")
            exec(python_code, {})
    except FileNotFoundError:
        print(f"{RED}❌ फ़ाइल नहीं मिली: {file_path}{RESET}")
    except Exception as e:
        print(f"{YELLOW}⚠️ प्रोग्राम में त्रुटि:{RESET}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
