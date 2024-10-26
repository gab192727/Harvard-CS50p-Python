from pyfiglet import Figlet
import sys
import random

try:
    figlet = Figlet()
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"]:
            font = sys.argv[2]
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

    figlet.setFont(font=font)

    s = input("Input: ")
    print(f'''Output:
{figlet.renderText(s)}''')

except ValueError:
    sys.exit("Invalid Usage")


