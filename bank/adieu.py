import inflect
import sys

names = []
p = inflect.engine()

try:
    while True:
        name = input("Name:")
        names.append(name)

except EOFError:
    print(f"Adieu, adieu, to {p.join(names)}")
    sys.exit()
