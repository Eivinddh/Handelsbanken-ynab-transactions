import csv
from datetime import datetime

def convert_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='ISO-8859-1') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter=';')
        fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            if not any(row.values()):  # Check if the row is empty
                break
            date = datetime.strptime(row['Utført dato'], '%d.%m.%Y').strftime('%Y-%m-%d')
            outflow = abs(float(row['Beløp ut'])) if row['Beløp ut'] else ''
            inflow = row['Beløp inn']
            writer.writerow({
                'Date': date,
                'Payee': 'Brukskonto - Handelsbanken',
                'Memo': row['Melding/KID/Fakt.nr'],
                'Outflow': outflow if outflow else '',
                'Inflow': inflow if inflow else ''
            })

if __name__ == "__main__":
    input_file = 'input.csv'  # Replace with your input file path
    output_file = 'output.csv'  # Replace with your output file path
    convert_csv(input_file, output_file)