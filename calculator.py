import requests
from pprint import pprint
class Calculator(object):
    def __init__(self):
        self.adress = "https://api.coinmarketcap.com/v1/ticker/?convert=SEK&limit=0"
        self.response = requests.get(self.adress)
        self.data = self.response.json()
        pass
    def priceOfCoin(self, name, currency):
        for item in self.data:
            if item['id'] == name:
                if(currency == "USD"):
                    return item["price_usd"]

                else:
                    return item["price_" + currency.lower()]

    def sumOfCoins(self,coinList):
        pass

