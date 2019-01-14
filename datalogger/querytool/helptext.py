# Module is basically a dumping ground for various menus and help text blurbs the terminal may need.

def HelpText():
	print "------------------ INFO ---------------------"
	print "TD Ameritrade API Query Tool"
	print "Version 0.0.1\n"
	
	print "Command List:"
	print "history\t\t: Displays ticker price history candles."
	print "query\t\t: Pings the API for specific ticker data."
	print "markethours\t: Gets market open/closed status."
	print "quit\t\t: Quits the querytool terminal."
	print "---------------------------------------------"

def QuoteHelpText():
	print "\t Name: \t quote"
	print "\t Args: \t [symbol]"
	print "\t Func: \t Gets quote data for the ticker/symbol passed."
	
def PriceHistoryHelpText():
	print "\t Name: \t history"
	print "\t Args: \t [symbol] <'day'/'month'/'year'/'ytd'> <period> <'day'/'month'/'year'/'ytd'> <frequency>"
	print "\t Func: \t Gets candle history data for the specified symbol."

def MarketHoursHelpText():
	print "\t Name: \t markethours"
	print "\t Args: \t [market] <date>"
	print "\t Func: \t Gets market hours for the specified market. Default date and time is right now."
	
def AuthHelpText():
	print "\t Name: \t auth"
	print "\t Subcommands: \t set, get"
	print "\t Args:"
	print "\t Func: \t Function unimplemented."