import requests
import json

class API:

    # Constructor
    # Expects 'base' as cryptocurrency abbreviation - Coinbase API currently allows only 'BTC', 'ETH', 'LTC', 'BCH'
    # Expects 'currency' as abbreviation for the currency to get the value in, e.g. 'GBP' or 'USD'
    def __init__(self, base, currency):
        self.base = base
        self.currency = currency
        self.baseUrl = 'https://api.coinbase.com/v2/'
        print('API object created for coin ' + self.base + ' with ' + self.currency)

    # Makes HTTP GET request to given URL, returns response as JSON object
    def get(self, url):
        r = requests.get(url)
        return json.loads(r.text)

    # Makes HTTP POST request to given URL, returns response as JSON object
    # Expects POST data to be a JSON object
    def post(self, url, data):
        r = requests.post(url, data)
        return json.loads(r.text)

    # Fetch current price of coin from Coinbase API
    def getCurrentPrice(self):
        return self.get(self.baseUrl + 'prices/' + self.base + '-' + self.currency + '/spot/')

    # Fetch price of coin at the given date
    # Expects date to be 
    def getHistoricPrice(self, date):
        return 0

