import requests
from pprint import pprint
class Calculator(object):
    def __init__(self):
        self.adress = "https://api.coinmarketcap.com/v1/ticker/?convert=SEK&limit=0"
        self.response = requests.get(self.adress)
        self.data = self.response.json()
        pass
    def priceOfCoin(self, name, currency):
        # adress = "https://api.coinmarketcap.com/v1/ticker/" + name + "?convert=" + currency 
        # response = requests.get(adress)
        # data = response.json()
        # coin = data[0]
        for item in self.data:
            # pprint(item)
            if item['id'] == name:
                if(currency == "USD"):
                    return item["price_usd"]

                else:
                    return item["price_" + currency.lower()]

    def sumOfCoins(self,coinList):
        pass

