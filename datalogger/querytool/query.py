# Module is the top-level QueryTool class. It provides important global definitions, and
# constructs and sends JSON data.
from copy import deepcopy
import requests

import quotes
import candles

# Possible return value error codes.
ERR_NULL_VALUE			= 400
ERR_INVALID_AUTH		= 401
ERR_FORBIDDEN			= 403
ERR_NOT_FOUND			= 404

# Convenient path vairables.
API_KEY					= "GX4040"
API_CORE_PATH 			= "https://api.tdameritrade.com/v1/"
API_ACCOUNTS_SUFFIX 	= "accounts/"
API_AUTH_SUFFIX 		= "oauth2/token/"
API_INSTRUMENT_SUFFIX 	= "instruments/"
API_MARKETHOURS_SUFFIX 	= "marketdata/"
API_MOVERS_SUFFIX 		= "marketdata/"
API_CHAIN_SUFFIX 		= "marketdata/chains/"
API_PRICE_SUFFIX 		= "marketdata/"
API_QUOTE_SUFFIX 		= "marketdata/"
API_TRANSACTION_SUFFIX 	= "accounts/"
API_PREFERENCES_SUFFIX 	= "accounts/"
API_STREAMER_SUFFIX 	= "userprincipals/streamersubscriptionkeys/"
API_PRINCIPALS_SUFFIX 	= "userprincipals/"
API_WATCHLIST_SUFFIX 	= "accounts/"

# A direct interface to the TD Ameritrade API. Each method takes arguments specific
# to the query in the API.
class QueryTool(object):
	def __init__(self):
		self.successfulQueries 	= 0
		self.failedQueries		= 0
	
	def CancelOrder(self, accountID, orderID):
		print "Method Unimplemented"
		return
	
	def GetOrder(self, accountID, orderID):
		print "Method Unimplemented"
		return
		
	def GetOrderByPath(self,  accountID, maxResults, fromTime, toTime, status):
		print "Method Unimplemented"
		return
		
	def GetOrderByQuery(self, accountID, maxResults, fromTime, toTime, status):
		print "Method Unimplemented"
		return
		
	def PlaceOrder(self, accountID, order):
		print "Method Unimplemented"
		return
		
	def ReplaceOrder(self, accountID, orderID, order):
		print "Method Unimplemented"
		return
	
	def CreateSavedOrder(self, accountID, order):
		print "Method Unimplemented"
		return
		
	def DeleteSavedOrder(self, accountID, savedOrderID):
		print "Method Unimplemented"
		return
		
	def GetSavedOrder(self, accountID, savedOrderID):
		print "Method Unimplemented"
		return
		
	def GetSavedOrderByPath(self, accountID):
		print "Method Unimplemented"
		return
		
	def ReplacedSavedOrder(self, accountID, savedOrderID, order):
		print "Method Unimplemented"
		return
		
	def GetAccount(self, accountID, fields):
		print "Method Unimplemented"
		return
		
	def GetAccounts(self, fields):
		print "Method Unimplemented"
		return
		
	def PostAccessToken(self, grant_type, refresh_token, access_type, code, client_id, redirect_uri):
		print "Method Unimplemented"
		return
		
	def SearchInstruments(self, symbol, projection):
		print "Method Unimplemented"
		return
		
	def GetInstrument(self, cusip):
		print "Method Unimplemented"
		return
	
	# Valid date strings are (1) yyyy-MM-dd (2) yyyy-MM-dd'T'HH:mm:ssz
	def GetMarketHours(self, market, date):
		print "Method Unimplemented"
		return
	
	# Get top 10 (up or down) movers by value or percent for a particular market.
	def GetMovers(self, market, direction='up', change='percent'):
		path = API_CORE_PATH + API_MOVERS_SUFFIX
		suffix = "/movers"
		
		# Sterilize input text.
		dir = direction.lower()
		ch  = change.lower()
		
		# Setup JSON parameters.
		params = {  'apikey' : API_KEY,
					'direction': direction,
					'change' : change }
		
		# Construct full path and sent JSON GET request.
		fullpath = path + market + suffix
		temp = SendJSON(fullpath, params)
		
		# Display character for change type.
		if change == 'value':
			type = 'U'
		else:
			type = '%'
		
		# Display all 10 movers.
		ctx = len(temp)
		for i in range(0, ctx):
			print "-- [" + direction.upper() + "] --"
			print "Symbol: " + temp[i]['symbol']
			print "Description: " + temp[i]['description']
			print "Change: " + str(temp[i]['change']) + type
			print "Last: $" + str(temp[i]['last']) + " Volume: " + str(temp[i]['totalVolume'])
			print "----------"
		
		return deepcopy(temp)
		
	def GetOptionChain(self, symbol, contractType, strikeCount, includeQuotes, strategy, interval, strike, range, fromDate, toDate, volatility, underlyingPrice, interestRate, daysToExp, expMonth, optionType):
		print "Method Unimplemented"
		return
	
	# Returns a list of Candle objects, unsorted, for the specified time frame.
	def GetPriceHistory(self, symbol, periodType='day', period=2, frequencyType='minute', frequency=1, endDate=0, startDate=0, extendedHours=False):
		path = API_CORE_PATH + API_PRICE_SUFFIX
		suffix = "/pricehistory"
		
		# Sterilize the input text.
		pt = periodType.lower()
		p  = str(period)
		ft = frequencyType.lower()
		f  = str(frequency)
		
		# Setup JSON GET parameters.
		params = {  'apikey' : API_KEY,
					'periodType' : pt,
					'period' : p,
					'frequencyType' : ft,
					'frequency' : f,
					'needExtendedHoursData' : 'false' }
		
		# Add additional, option parameters.
		if endDate != 0 and startDate < endDate:
			params['endDate'] = endDate
			params['startDate'] = startDate
		if extendedHours == True:
			params['needExtendedHoursData'] = 'true'

		# Setup full API path and send JSON GET request.
		fullpath = path + symbol + suffix
		temp = SendJSON(fullpath, params)
		
		# If response was empty, something went wrong.
		if not temp:
			print "Invalid JSON parameter."
		else:
			numcandles = len(temp["candles"])
			clist = []
			
			# Create a candle object for each piece of
			# candle data recieved.
			for i in range(0, numcandles):
				c = candles.Candle(temp["candles"][i])
				clist.append(c)
				c.PrintAttributes()
		
		print "Retrieved " + str(numcandles) + " candles."
		
		return deepcopy(clist)
		
	def GetQuotes(self, symbols):
		path   = API_CORE_PATH + API_QUOTE_SUFFIX
		suffix = "/quotes"
		params = { 'apikey' : API_KEY }
		
		quote_array = []
		
		# Send a JSON request for each symbol requested.
		for sym in symbols:
			
			# Construct full API path.
			fullpath = path + sym + suffix
			
			# Send JSON GET request.
			temp = SendJSON(fullpath, params)
			
			# If response was empty, something went wrong.
			if not temp:
				print "Invalid symbol name."
			else:
				type = quotes.GetQuoteType(sym, temp)
				
				# Instantiate a Quote subclass specific
				# to the quote type.
				if type == 'EQUITY':
					obj = quotes.EquityQuote(temp)
					obj.PrintAttributes()
					quote_array.append(obj)
				elif type == 'MUTUAL_FUND':
					obj = quotes.MutualFundQuote(temp)
					obj.PrintAttributes()
					quote_array.append(obj)
				else:
					print temp
		
		return deepcopy(quote_array)
		
	def GetTransaction(self, accountID, transactionID):
		print "Method Unimplemented"
		return
	
	def GetTransactions(self, accountID, type, symbol, startDate, endDate):
		print "Method Unimplemented"
		return
		
	def GetPreferences(self, accountID):
		print "Method Unimplemented"
		return
		
	def GetSubscriptionKeys(self, accountIDs):
		print "Method Unimplemented"
		return
		
	def GetUserPrincipals(self, fields):
		print "Method Unimplemented"
		return
		
	def SetPreferences(self, accountID, preferences):
		print "Method Unimplemented"
		return
		
	def CreateWatchlist(self, accountID, watchlist):
		print "Method Unimplemented"
		return
		
	def DeleteWatchlist(self, accountID, watchlistID):
		print "Method Unimplemented"
		return
	
	def GetWatchlist(self, accountID, watchlistID):
		print "Method Unimplemented"
		return
		
	def GetWatchlists(self, accountID):
		print "Method Unimplemented"
		return
		
	def GetAllWatchlists(self):
		print "Method Unimplemented"
		return
		
	def ReplaceWatchlist(self, accountID, watchlistID, watchlist):
		print "Method Unimplemented"
		return
		
	def UpdateWatchlist(self, accountID, watchlistID, watchlist):
		print "Method Unimplemented"
		return

# Send a JSON request given a URL address and JSON parameters.
def SendJSON(address, parameters):
	r = requests.get(url = address, params = parameters)
	data = r.json()
	
	return data

# Doesn't work.
def QueryTool_SetAPIKey(key):
	API_KEY = key
	return

# Return currently used API key.
def QueryTool_GetAPIKey():
	return API_KEY