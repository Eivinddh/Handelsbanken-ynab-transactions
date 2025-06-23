import os
import re
import sys

# Usage: python auto_input_file.py
# This script will look for a file named 'Transactions <date>.csv' and process it with convert-brukskonto.py if found.

def find_transactions_file():
    # Match files like 'Transactions June 22 2025' (with or without .csv extension)
    pattern = re.compile(r'^Transactions [A-Za-z]+ \d{1,2} \d{4}(\.csv)?$')
    for filename in os.listdir('.'):
        if pattern.match(filename):
            return filename, 'brukskonto'
        if filename == 'Kontobevegelser.csv':
            return filename, 'kredittkort'
    return None, None

def main():
    transactions_file, filetype = find_transactions_file()
    if not transactions_file:
        print("No 'Transactions <date>.csv' or 'Kontobevegelser.csv' file found.")
        sys.exit(1)
    if filetype == 'brukskonto':
        print("Using convert-brukskonto.py for:", transactions_file)
        os.system(f'python3 convert-brukskonto.py "{transactions_file}" output.csv')
        print(f"Processed '{transactions_file}' with convert-brukskonto.py.")
    elif filetype == 'kredittkort':
        print("Using convert-kredittkort.py for:", transactions_file)
        os.system(f'python3 convert-kredittkort.py "{transactions_file}" output.csv')
        print(f"Processed '{transactions_file}' with convert-kredittkort.py.")

if __name__ == "__main__":
    main()
