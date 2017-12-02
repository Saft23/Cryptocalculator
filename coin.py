#!/usr/bin/python3
from pprint import pprint
from calculator import Calculator
from wallet import Wallet
from expenses import Expenses
import sys

calculator = Calculator()
wallet = Wallet()
expenses = Expenses()

#Avalible commands

#sum percent
#sum sek
#expenses
#wallet usd
#wallet sek
#wallet e

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
            print(str(sumExpenses) + " sek")

    if(sys.argv[1] == "wallet"):
        if(sys.argv[2] == "usd"):
            sumWallet = wallet.calculateWorth("usd")
            print(str(sumWallet) + " usd")
        elif(sys.argv[2] == "sek"):
            sumWallet = wallet.calculateWorth("sek")
            print(str(sumWallet) + " sek")
        elif(sys.argv[2] == "e"):
            wallet.editWallet()
            
else:
    print("Give the program more arguments")

