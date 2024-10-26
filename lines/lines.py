import sys

argument = sys.argv
try:
    if len(argument) > 2:
        sys.exit('Too many command-line arguments ')

    if not argument[1].endswith('.py'):
        sys.exit('Not a Python file')

except IndexError:
    sys.exit('Too few command-line arguments')

try:
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        count_of_lines = 0
        for line in file:
            line = line.strip()
            if line.startswith('#') or line == '':
                continue
            else:
                count_of_lines += 1

    print(count_of_lines)

except FileNotFoundError:
    sys.exit('File does not exist')
