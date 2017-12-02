from calculator import Calculator
import os
class Wallet(object):
    wallet = None
    walletArray = []
    def __init__(self):
        relativePath = os.path.dirname(__file__)
        self.path = os.path.join(relativePath,'.wallet')
        if not(os.path.isfile(self.path)):
            self.wallet=open(self.path, 'w+')
            self.wallet.close()

    def calculateWorth(self, currency):
        self.calculator = Calculator()
        self.wallet=open(self.path)
        walletlist = self.wallet.read().split('\n')
        self.wallet.close()
        walletlist.pop()
        returnValue = 0.0
        for item in walletlist:
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
            returnValue = returnValue + (coinWorth * numCoin)
            self.walletArray.append(returnValue)

        return returnValue

    def editWallet(self):
        os.system("vim " + self.path)



