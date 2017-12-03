#!/usr/bin/python3
from pprint import pprint
from calculator import Calculator
from wallet import Wallet
from expenses import Expenses
import sys

wallet = Wallet()
expenses = Expenses()

#Avalible commands

#sum percent
#sum sek
#expenses
#wallet usd
#wallet sek
#wallet e
#value coin currency

if(len(sys.argv) > 1):

    if(sys.argv[1] == "sum"):
        sumExpenses = expenses.calculateExpenses()
        if(sys.argv[2] == "percent"):
            sumWallet = wallet.calculateWorth("sek")
            final = sumWallet / sumExpenses
            final = final - 1
            final = final * 100
            final = int(final)
            print(str(final) + "%")
        else:
            sumWallet = wallet.calculateWorth("sek")
            result = sumWallet - sumExpenses
            print(str(result) + "sek")

    if(sys.argv[1] == "expenses"):
        if(len(sys.argv) > 2):
            if(sys.argv[2] == "e"):
                expenses.editExpenses()
        else:
            sumExpenses = expenses.calculateExpenses()
            print(str(sumExpenses) + "sek")

    if(sys.argv[1] == "wallet"):
        if(sys.argv[2] == "e"):
            wallet.editWallet()
        elif(sys.argv[2] == "distribution" or sys.argv[2] == "dist"):
            wallet.distribution()
        else:
            sumWallet = wallet.calculateWorth(sys.argv[2])
            if(sumWallet == 0):
                print("Unkown currency or empty wallet")
            print(str(sumWallet) + sys.argv[2].upper())
            
    if(sys.argv[1] == "value"):
        if(len(sys.argv) > 3):
            calculator = Calculator()
            print(str(calculator.priceOfCoin(sys.argv[2], sys.argv[3])) + sys.argv[3])
        else:
            print("Value needs cryptoname and currency as argument")

    if(sys.argv[1] == "diversify"):
        if(len(sys.argv) > 4):
            calculator = Calculator()
            args = sys.argv
            value = args[2]
            currency = args[3]
            args.pop(0);args.pop(0);args.pop(0);args.pop(0)
            coins = args
            calculator.diversify(value, currency, coins)
        else:
            print("Need more arguments(at least 3). Ex. Value Currency Coin Coin ...")

else:
    print("Give the program more arguments")

