import json
from exchanges.coinbase.coinbase import coinbaseAPI

with open('config.json') as config_file:
    config = json.load(config_file)
base = config['base']
currency = config['currency']
coinbaseAPI = coinbaseAPI(base, currency)

test = coinbaseAPI.getCurrentPrice()
print(test)