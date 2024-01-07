import requests
import sys
import json

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = response.json()
    bitcoin_amount = result["bpi"]["USD"]["rate_float"]
    total_amount = bitcoin_amount * n
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    pass
