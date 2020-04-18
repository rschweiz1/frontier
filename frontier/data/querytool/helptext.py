# Module is basically a dumping ground for various menus and help text blurbs the terminal may need.

def HelpText():
	print("""
		  ------------------ INFO ---------------------
		  TD Ameritrade API Query Tool
	      Version 0.0.1
	
	      Command List:
	      history\t\t: Displays ticker price history candles.
	      query\t\t: Pings the API for specific ticker data.
	      markethours\t: Gets market open/closed status.
	      quit\t\t: Quits the querytool terminal.
	      ---------------------------------------------
		  """)

def QuoteHelpText():
	print("""
	      \t Name: \t quote
	      \t Args: \t [symbol]
	      \t Func: \t Gets quote data for the ticker/symbol passed.
		  """)
	
def PriceHistoryHelpText():
	print("""
		  \t Name: \t history
	      \t Args: \t [symbol] <'day'/'month'/'year'/'ytd'> <period> <'day'/'month'/'year'/'ytd'> <frequency>
	      \t Func: \t Gets candle history data for the specified symbol.
		  """)

def MarketHoursHelpText():
	print("""
		  \t Name: \t markethours
		  \t Args: \t [market] <date>
		  \t Func: \t Gets market hours for the specified market. Default date and time is right now.
		  """)
	
def AuthHelpText():
	print("""
		  \t Name: \t auth
	      \t Subcommands: \t set, get
	      \t Args:
	      \t Func: \t Function unimplemented.
		  """)