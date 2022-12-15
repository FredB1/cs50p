import requests
import sys

try:
    btc= float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass
except (ValueError):
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
data = response.json()["bpi"]["USD"]["rate_float"] * btc
print(f"${data:,.4f}")