## Query Tool ##
The Query Tool is a Python abstraction of the TD Ameritrade Developer's API. It
supports various commands to interface with it, including getting quotes, posting
orders, and modifying account preferences.

Begin a terminal session by navigating to the /datalogger directory:

`python terminal.py`

From here, a double-carat (>>) symbol will appear, and is ready to accept querytool commands.

##### Command List #####
NOTE: Brackets [ ] denote required arguments.

+ **Command**: ```help```  
**Subcommands**: None  
**Description**: Displays querytool basic information.  
**Example**: ```>> help```

+ **Command**: ```quit```  
**Subcommands**: None  
**Description**: Exits the querytool terminal back to the command line.  
**Example**: ```>> quit```  

+ **Command**: ```history```  
**Subcommands**: None  
**Description**: Displays candle data history for a given ticker and time frame.  
**Example**: ```>> history AAPL```  

+ **Command**: ```query```  
**Subcommands**: ```quote, movers```  
**Description**: Queries specific data from the API.  

 *Subcommand*: ```quote```  
*Arguments*: ```[symbol]```  
*Description*: Returns market data for the specified ticker.  
*Examples*:  
```>> query quote IEC```  
   
 *Subcommand*: ```movers```  
*Arguments*: ```[market] <direction> <change-type>```  
*Description*: Displays the top 10 movers for a given market, either up/down and percent/value.  
*Examples*:   
```>> query movers $COMPX```   
```>> query movers $COMPX down value```  


####### Miscellaneous #####
Currently, querytool is in its infancy and only supports a few commands, which are relatively
buggy. Most importantly, it sets up classes and data structures that facilitate database creation,
loading, and exporting to files. Similarly, it serves as an interface to create small datasets
for analysis and training machine learning.

Future improvements include automated scripting and database linking.