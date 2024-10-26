import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    bitcoin_amount = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a valid number")
    sys.exit(1)

data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

usd_rate = float(data['bpi']['USD']['rate'].replace(',', ''))

converted_amount = bitcoin_amount * usd_rate

formatted_amount = "{:,.4f}".format(converted_amount)

print(f"${formatted_amount}")
