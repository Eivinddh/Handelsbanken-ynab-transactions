import csv
from datetime import datetime

def convert_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter='\t')
        fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            date = datetime.strptime(row['Utført dato'], '%d.%m.%Y').strftime('%Y-%m-%d')
            outflow = row['Beløp ut']
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