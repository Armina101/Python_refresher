import requests

API_KEY = "fca_live_xf0aoC2KZ77WJcveC4NzCOHMVj6ehSBQ3qccHS4C"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = {"USD", "CAD", "EUR", "AUD", "CNY"}

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        return data
    except Exception as e:
        print(e)
        return None

data = convert_currency("CAD")
     