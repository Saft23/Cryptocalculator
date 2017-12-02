# Cryptocalculator
Structure for the .files  
  
//.wallet  
bitcoin: 13.23  
iota: 323.345  
ethereum: 942.4561313  
//ENDOFFILE  
  
  
//.expences in sek  
3451  
45151  
5613  
2345  
//ENDOFFILE  
  
  
To make sure you edit the corrent file, use "coin wallet e" and "coin expenses e" to edit the dotfiles.  
  
Available arguments/commands:  
```
sum percent             //Prints the percentage of the value compared to the expenses  
sum sek                 //Prints the difference between value and expenses  
expenses                //Prints the expenses  
expenses e              //Edits the expenses file  
wallet usd              //Prints the value in the wallet in usd  
wallet sek              //Prints the value in the wallet in sek  
wallet e                //Edits the wallet file  
value coin currency     //Prints the current price of the given coin in the given currency  
```
  
  
  
  
  
The guidelines regarding the API:  
Please limit requests to no more than 10 per minute.  
Endpoints update every 5 minutes.  

  
  
  
todo:  
Optimize api requests  
bitfinex api key  
bittrex api key  
coinbase api??  
fix parsing in .wallet  

