#!/usr/bin/python3
from pprint import pprint
from calculator import Calculator
from wallet import Wallet
from expenses import Expenses
import sys

wallet = Wallet()
expenses = Expenses()


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
            calculator = Calculator()
            expensesCurrency = expenses.currency
            currencyChanger = calculator.currency(expensesCurrency.upper())
            rates = calculator.currency(expensesCurrency)
            sumWallet = wallet.calculateWorth('usd')
            sumExpenses = sumExpenses / currencyChanger
            result = sumWallet - sumExpenses
            changer = calculator.currency(sys.argv[2].upper())
            if(changer == 0):
                changer = 1
            result = changer * result
            print(str(("%.2f" % (result))) + sys.argv[2])

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
        elif(sys.argv[2] == "list"):
            if(len(sys.argv) > 3):
                if(sys.argv[3] == "distribution" or sys.argv[3] == "dist" or sys.argv[3] == "percent" ):
                    wallet.distribution()
                elif(sys.argv[3] == "value"):
                    if(len(sys.argv) > 4):
                        wallet.distributionAndWorth(sys.argv[4])
                    else:
                        print("Need more arguments")
            else: 
                wallet.listWallet()
        elif(sys.argv[2] == "add"):
            if(len(sys.argv) > 4):
                wallet.add(sys.argv[3], sys.argv[4])
            else:
                print("Need more arguments")
        elif(sys.argv[2] == "remove"):
            if(len(sys.argv) > 4):
                wallet.add("-" + sys.argv[3], sys.argv[4])
            else:
                print("Need more arguments")
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

