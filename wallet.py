from calculator import Calculator
import os
class Wallet(object):
    wallet = None
    def __init__(self):
        relativePath = os.path.dirname(__file__)
        self.path = os.path.join(relativePath,'.wallet')
        if not(os.path.isfile(self.path)):
            self.wallet=open(self.path, 'w+')
            self.wallet.close()

    def getWalletArray(self, currency, coinOrValue):
        self.calculator = Calculator()
        self.wallet=open(self.path)
        walletlist = self.wallet.read().split('\n')
        self.wallet.close()
        walletlist.pop()
        returnValue = []
        returnCoin = []
        for item in walletlist:
            if(item == ""):
                item = "bitcoin: 0"
            fin = item.find(':')
            beg = 0
            coin = ""
            numCoin = ""
            while(beg < fin):
                coin = coin + item[beg]
                beg = beg +1
            while(fin+2 < len(item)):
                numCoin = numCoin + item[fin+2]
                fin = fin +1
            coinWorth = float(self.calculator.priceOfCoin(coin,currency.upper()))
            numCoin = float(numCoin)
            returnValue.append(coinWorth * numCoin)
            returnCoin.append(coin)
        if(coinOrValue == 'coin'):
            return returnCoin
        elif(coinOrValue == 'value'):
            return returnValue

    def distribution(self):
        coinArray = self.getWalletArray('usd', 'coin')
        valueArray = self.getWalletArray('usd', 'value') 
        total = self.calculateWorth('usd') 
        i = 0
        for coin in coinArray:
            print(coin + ": " + ("%.2f" % ((valueArray[i] / total)*100)) + "%")
            i = i +1


    def calculateWorth(self, currency):
        return sum(self.getWalletArray(currency, 'value'))

    def editWallet(self):
        os.system("vim " + self.path)



