import csv
from datetime import datetime
import sys

def convert_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8-sig') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter=';')
        fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            if not any(row.values()):  # Check if the row is empty
                break
            date = datetime.strptime(row['Dato'], '%d.%m.%Y').strftime('%Y-%m-%d')
            description = row['Beskrivelse'].strip('="')
            amount = float(row['Beløp'].replace(',', '.'))  # Convert Beløp to float
            outflow = abs(amount) if amount < 0 else ''
            inflow = amount if amount > 0 else ''
            writer.writerow({
                'Date': date,
                #'Payee': 'Brukskonto - Handelsbanken' if inflow != '' and inflow > 0 else 'Kredittkort - Handelsbanken',
                'Memo': description,
                'Outflow': outflow,
                'Inflow': inflow
            })

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input.csv'  # Default if no argument is given
    output_file = 'output.csv'  # Replace with your output file path
    convert_csv(input_file, output_file)