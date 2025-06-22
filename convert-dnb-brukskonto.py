import csv
from datetime import datetime

def convert_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8-sig') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter=';')
        fieldnames = ['Date', 'Payee', 'Memo', 'Outflow', 'Inflow']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            print(row)  # Debugging line to check the row content
            if not any(row.values()):  # Skip empty rows
                continue
            # Parse date in format '18/06/2025' (day/month/year)
            date = datetime.strptime(row['Dato'], '%d/%m/%Y').strftime('%Y-%m-%d')
            memo = row['Forklaring'].strip()
            # Remove spaces from numbers for correct float conversion
            outflow = row['Ut fra konto'].replace(' ', '').replace(',', '.').strip()
            inflow = row['Inn på konto'].replace(' ', '').replace(',', '.').strip()
            outflow = float(outflow) if outflow else ''
            inflow = float(inflow) if inflow else ''
            writer.writerow({
                'Date': date,
                'Payee': 'Brukskonto',
                'Memo': memo,
                'Outflow': outflow,
                'Inflow': inflow
            })

if __name__ == "__main__":
    input_file = 'input.csv'  # Replace with your input file path
    output_file = 'output.csv'  # Replace with your output file path
    convert_csv(input_file, output_file)
