# Module manages the user interface terminal, accepting commands and displaying information.
# It is the entry point if running from main.
import argparse
import sys

# TODO Wrapper for QueryTool.GetMarketHours()
def MarketHoursCommand(tokens):
	qt = query.QueryTool()
	
	argc = len(tokens)
	
	# markethours [market] <date>
	if argc < 2:
		print "Usage: "
		helptext.MarketHoursHelpText()
	else:
		if argc == 2:
			qt.GetMarketHours(tokens[1])
		elif argc == 3:
			qt.GetMarketHours(tokens[1], tokens[2])
		else:
			print "Too many arguments."
			
	return
			
# Usage: query [subcommand] <subcommand-arguments>
#
# Subcommands:
#		'quote'    : Returns market data from the specified ticker.
#		arguments: 
#			[symbol] - Ticker symbol
#		examples:	(1) query quote AAPL
#
#		'movers'   : Returns top 10 moving tickers for a given market
#		arguments:
#			[market]		- $COMPX, $DJI, $SPX.X 
#			<direction>		- up, down
#			<change-type>	- percent, value
#		examples: (1) query movers $COMPX	(2) query movers $DJI down value
#	
def QueryCommand(tokens):
	qt = query.QueryTool()
	
	argc = len(tokens)
	
	# Type of query.
	type = tokens[1]
	
	if type == "quote":
		if argc < 3:
			print "Usage: "
			helptext.QuoteHelpText()
		else:
			s = []
			s.append(tokens[2])

			qt.GetQuotes(s)
	elif type == "movers":
		if argc < 3:
			print "Usage: "
			QuoteHelpText()
		else:
			mkt = tokens[2]
			if argc == 3:
				qt.GetMovers(mkt)
			elif argc == 4:
				qt.GetMovers(mkt, direction=tokens[3])
			elif argc == 5:
				qt.GetMovers(mkt, direction=tokens[3], change=tokens[4])
			else:
				print "Too many arguments."
	return

# Usage: history [symbol] <period-type> <period> <frequency-type> <frequency> <endDate>	<startDate> <extendedHours>
# Arguments:
#	[symbol] 		 - Ticker symbol
#	<period-type> 	 - Type of period to show: 	(day, month, year, ytd)
#	<period>		 - Number of periods to show. (Default: Varies)
#	<frequency-type> - Frequency in which new candle is formed:	(day, month, year, ytd)
#	<frequency>		 - Number of frequency-type to be included in each candle. (Default: 1)
#	<extendedHours>  - Returned price history includes extended trading hours (Default: False)

# Note: If using <period, leave these fields blank.
#	TODO<endDate>		 - Lookup end date (milliseconds since epoch).
#	TODO<startDate>		 - Lookup start date (milliseconds since epoch).
#
# Examples: 
#	(1) history AAPL day 2 minute 1
#	
def PriceHistoryCommand(tokens):
	qt = query.QueryTool()
	
	argc = len(tokens)
	
	if argc < 2:
		print "Usage: "
		helptext.PriceHistoryHelpText()
	else:
		sym = tokens[1]
		if argc == 2:
			qt.GetPriceHistory(sym)
		elif argc == 3:
			qt.GetPriceHistory(sym, periodType=tokens[2])
		elif argc == 4:
			qt.GetPriceHistory(sym, periodType=tokens[2], period=str(tokens[3]))
		elif argc == 5:
			qt.GetPriceHistory(sym, periodType=tokens[2], period=str(tokens[3]), frequencyType=tokens[4])
		elif argc == 6:
			qt.GetPriceHistory(sym, periodType=tokens[2], period=str(tokens[3]), frequencyType=tokens[4], frequency=str(tokens[5]))
		else:
			print "Too many arguments."

# TODO These don't really work.
def AuthCommand(tokens):
	
	argc = len(tokens)
	
	if argc < 3:
		print "Usage:"
		helptext.AuthHelpText()
	else:
		sub  = tokens[1]
		type = tokens[2]
		
		if sub == "set" and type == "API_KEY":
			key1 = raw_input("Enter new API key: ")
			#type(key1)
			key2 = raw_input("Retype new API key: ")
			#type(key2)
			
			if key1 != key2:
				print "Error, key entires do not match."
			else:
				query.QueryTool_SetAPIKey(key1)
			
		elif sub == "get" and type == "API_KEY":
			key = query.QueryTool_GetAPIKey()
			print key
		else:
			print "Unrecognized command."

	return
	
def Dispatch(tokens):
	command = tokens[0]
	
	# Interpret user command.
	if command == "help":
		helptext.HelpText()
	elif command == "query":
		QueryCommand(tokens)
	elif command == "history":
		PriceHistoryCommand(tokens)
	elif command == "markethours":
		MarketHoursCommand(tokens)
	elif command == "auth":
		AuthCommand(tokens)
	else:
		print "'" + command + "'" + " is not a valid command."
			
	return
	
def Run():

	# Wait for and read user input.
	text = raw_input(">> ")
	type(text)
	
	while text != "quit":
		
		# Break the input into tokens and pass to dispatch function.
		tokens 	= text.split()
		Dispatch(tokens)
		
		# Wait for and read user input.
		text = raw_input(">> ")
		type(text)

	print "Program Exit."

	return
	
if __name__ == "__main__":
	# Include the path to the querytool directory.
	sys.path.insert(0, './querytool')
	
	from querytool import query
	from querytool import helptext

	Run()