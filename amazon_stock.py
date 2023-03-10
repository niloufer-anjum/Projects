import json
import requests

params = {
    "function": "GLOBAL_QUOTE",
    "symbol": "AMZN",
    "apikey": "BZ9ME6Q3OOMGINJ8"
}

url = "https://www.alphavantage.co/query?"
response = requests.get(url, params)

if (response.status_code == 200):
    quote = response.json()['Global Quote']['05. price']
    print(quote)