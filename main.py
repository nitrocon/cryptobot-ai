import json
from coinbase import API

with open('config.json') as config_file:
    config = json.load(config_file)
base = config['base']
currency = config['currency']
API = API(base, currency)

test = API.getCurrentPrice()
print(test)