import json
from exchanges.coinbase.coinbase import coinbaseAPI

with open('exchanges/coinbase/coinbase.json') as coinbase_config_file:
    config = json.load(coinbase_config_file)
base = config['base']
currency = config['currency']
coinbaseAPI = coinbaseAPI(base, currency)

test = coinbaseAPI.getCurrentPrice()
print(test)