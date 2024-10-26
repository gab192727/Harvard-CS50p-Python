import csv
import sys

try:
    argument = sys.argv
    if len(argument) > 3:
        sys.exit('Too many command-line arguments ')

    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])


            writer.writeheader()


            for row in reader:

                last, first = row['name'].split(', ')

                writer.writerow({'first': first, 'last': last, 'house': row['house']})
    except FileNotFoundError:
        if input_file not in FileNotFoundError:
            sys.exit(f'Could not read {input_file}')
        else:
            sys.exit(f'Could not read {output_file}')

except IndexError:
    sys.exit('Too few command-line arguments')
