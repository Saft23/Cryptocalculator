import requests
import os
from pprint import pprint
import json
import time
class Calculator(object):
    def __init__(self):
        relativePath = os.path.dirname(__file__)
        self.coinCachePath = os.path.join(relativePath,'.coincache.json')
        self.currencyCachePath = os.path.join(relativePath,'.currencycache.json')
        if not(os.path.isfile(self.coinCachePath)):
            print("Created coin cache")
            self.adress = "https://api.coinmarketcap.com/v1/ticker/?limit=0"
            self.response = requests.get(self.adress)
            self.data = self.response.json()
            json.dump(self.data, open(self.coinCachePath,'w'))
            
        if not(os.path.isfile(self.currencyCachePath)):
            print("Created currency cache")
            self.currencyAdress = "https://api.fixer.io/latest?base=USD"
            self.currencyResponse = requests.get(self.currencyAdress)
            self.currencyData = self.currencyResponse.json()
            json.dump(self.currencyData, open(self.currencyCachePath,'w'))

        with open('.coincache.json') as json_data:
                self.data = json.load(json_data)
        with open('.currencycache.json') as json_data:
                self.currencyData = json.load(json_data)

        currentTime = int(time.time())
        updateTime = int(self.data[0]['last_updated'])
        if(updateTime < (currentTime - 600)):
            self.updateCache() 
        



    def priceOfCoin(self, name, currency):
        for item in self.data:
            if item['id'] == name:
                if(currency == "USD"):
                    return item["price_usd"]

                else:
                    return float(item["price_usd"])*self.currency(currency)

    def currency(self, currency):
        try:
            return self.currencyData['rates'][currency]
        except Exception: 
            return 0

    def updateCache(self):
        print("Updated cache")
        self.adress = "https://api.coinmarketcap.com/v1/ticker/?limit=0"
        self.response = requests.get(self.adress)
        self.data = self.response.json()
        json.dump(self.data, open('.coincache.json','w'))
        self.currencyAdress = "https://api.fixer.io/latest?base=USD"
        self.currencyResponse = requests.get(self.currencyAdress)
        self.currencyData = self.currencyResponse.json()
        json.dump(self.currencyData, open('.currencycache.json','w'))
        pass
