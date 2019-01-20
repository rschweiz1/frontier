# Module manages the user interface terminal, accepting commands and displaying information.
# It is the entry point if running from main.


import argparse
import sys

def InstrumentsCommand(tokens):
	
	qt = query.QueryTool()
	argc = len(tokens)
	
	if argc < 2:
		print("Usage:")
	else:
		if argc == 2:
			qt.SearchInstruments(tokens[1])
		elif argc == 3:
			qt.SearchInstruments(tokens[1], projection=tokens[2])
		else:
			print("Too many arguments.")
	
	return

def MarketHoursCommand(tokens):
	"""
	Usage: markethours [market] <date>

	Notes: [market] can be any one of: EQUITY, OPTION, FUTURE, BOND, FOREX
	"""
	qt = query.QueryTool()

	argc = len(tokens)

	# markethours [market] <date>
	if argc < 2:
		print("Usage:")
		helptext.MarketHoursHelpText()
	else:
		if argc == 2:
			qt.GetMarketHours(tokens[1])
		elif argc == 3:
			qt.GetMarketHours(tokens[1], tokens[2])
		else:
			print("Too many arguments.")

	return

def QuoteCommand(tokens):

	qt = query.QueryTool()
	argc = len(tokens)
	
	if argc < 2:
		print("Usage: ")
		helptext.QuoteHelpText()
	else:
		sym = []
		sym.append(tokens[1])
		
		qt.GetQuotes(sym)

	return
	
def MoversCommand(tokens):

	qt = query.QueryTool()
	argc = len(tokens)
	
	if argc < 2:
		print("Usage: ")
	else:
		mkt = tokens[1]
		if argc == 2:
			qt.GetMovers(mkt)
		elif argc == 3:
			qt.GetMovers(mkt, direction=tokens[2])
		elif argc == 4:
			qt.GetMovers(mkt, direction=tokens[2], change=tokens[3])
		else:
			print("Too many arguments.")
			
	return

def PriceHistoryCommand(tokens):
	"""
	Usage: history [symbol] <period-type> <period> <frequency-type> <frequency> <endDate>	<startDate> <extendedHours>
	Arguments:
		[symbol] 		 - Ticker symbol
		<period-type> 	 - Type of period to show: 	(day, month, year, ytd)
		<period>		 - Number of periods to show. (Default: Varies)
		<frequency-type> - Frequency in which new candle is formed:	(day, month, year, ytd)
		<frequency>		 - Number of frequency-type to be included in each candle. (Default: 1)
		<endDate>		 - Lookup end date (milliseconds since epoch).
		<startDate>		 - Lookup start date (milliseconds since epoch).
		<extendedHours>  - Returned price history includes extended trading hours (Default: False)
	"""
	qt = query.QueryTool()

	argc = len(tokens)

	if argc < 2:
		print("Usage: ")
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
		elif argc == 7:
			qt.GetPriceHistory(sym, periodType=tokens[2], period=str(tokens[3]), frequencyType=tokens[4], frequency=str(tokens[5]), endDate=str(tokens[6]))
		elif argc == 8:
			qt.GetPriceHistory(sym, periodType=tokens[2], period=str(tokens[3]), frequencyType=tokens[4], frequency=str(tokens[5]), endDate=str(tokens[6]), startDate=str(tokens[7]))
		elif argc == 9:
			ext = False
			if tokens[8] == 'true' or tokens[8] == 'True' or tokens[8] == 'TRUE':
				ext = True

			qt.GetPriceHistory(sym, periodType=tokens[2], period=str(tokens[3]), frequencyType=tokens[4], frequency=str(tokens[5]), endDate=str(tokens[6]), startDate=str(tokens[7]), extendedHours=ext)
		else:
			print("Too many arguments.")

def Dispatch(tokens):
	command = tokens[0]

	# Interpret user command.
	if command == "help":
		helptext.HelpText()
	elif command == "quote":
		QuoteCommand(tokens)
	elif command == "history":
		PriceHistoryCommand(tokens)
	elif command == "markethours":
		MarketHoursCommand(tokens)
	elif command == "movers":
		MoversCommand(tokens)
	elif command == "instruments":
		InstrumentsCommand(tokens)
	else:
		print("'" + command + "'" + " is not a valid command.")

	return

def Run():

	# Wait for and read user input.
	text = input(">> ")
	type(text)

	while text != "quit":

		# Break the input into tokens and pass to dispatch function.
		tokens 	= text.split()
		Dispatch(tokens)

		# Wait for and read user input.
		text = input(">> ")
		type(text)

	print("Program Exit.")

	return

if __name__ == "__main__":
	# Include the path to the querytool directory.
	sys.path.insert(0, './querytool')

	from querytool import query
	from querytool import helptext

	Run()
