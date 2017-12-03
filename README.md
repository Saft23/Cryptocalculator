# Cryptocalculator

**Description**    
This program is designed for users that want to track their cryptocurrency  
and calculate profits, distributions, expenses etc..  
  
  
Structure for the .files    
  
//.wallet  
bitcoin: 13.23  
iota: 323.345  
ethereum: 942.4561313  
//ENDOFFILE  
  
  
//.expences //Definition of currency on the first line. Ex, usd, sek, eur  
sek  
3451.53  
45151  
5613  
2345  
//ENDOFFILE  
  
  
To make sure you edit the corrent file, use "coin wallet e" and "coin expenses e" to edit the dotfiles.  
  
Available arguments/commands:  
```
sum percent             //Prints the percentage of the value compared to the expenses  
sum usd                 //Prints the difference between value and expenses in usd
sum ___                 //Prints the difference between value and expenses if the currency is avalible
  
expenses                //Prints the expenses  
expenses e              //Edits the expenses file  
expenses add *value*	//Add an expense
expenses remove *value* //Remove *value* expense from expenses
  
wallet *usd*                        //Prints the value in the wallet in usd   
wallet ___                          //Prints the value in the wallet in ___ if the currency is available   
wallet e                            //Edits the wallet file   
wallet add *value* *coin*           //Add value amount of coins to wallet  
wallet remove *value* coin*	    //Remove value amount of coins to wallet  
wallet list		            //List your wallet   
wallet list dist	            //Show the value distribution of the coins in the wallet  
            distribution	    //As above   
	    percent	            //As above   
	    value *currency*	    //Show the value instead of percent   
  
value *coin* *currency*	//Prints the current price of the given coin in the given currency  
  
diversify *value* *currency* *coin* *coin* *...* 	//Distribute your money to get equal value of coins
```
  
  
  
  
  
todo:  
~~Optimize api requests~~  
bitfinex api key  
bittrex api key  
coinbase api??  
fix parsing in .wallet - Quick fix
  
  
  
Contributors: LampaaN
