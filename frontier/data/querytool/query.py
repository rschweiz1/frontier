# Module is the top-level QueryTool class. It provides important global definitions, and
# constructs and sends JSON data.
from copy import deepcopy
import requests
import datetime

import quotes
import candles
import instruments

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

	'''
	def CancelOrder(self, accountID, orderID):
		print("Method Unimplemented")
		return

	def GetOrder(self, accountID, orderID):
		print("Method Unimplemented")
		return

	def GetOrderByPath(self,  accountID, maxResults, fromTime, toTime, status):
		print("Method Unimplemented")
		return

	def GetOrderByQuery(self, accountID, maxResults, fromTime, toTime, status):
		print("Method Unimplemented")
		return

	def PlaceOrder(self, accountID, order):
		print("Method Unimplemented")
		return

	def ReplaceOrder(self, accountID, orderID, order):
		print("Method Unimplemented")
		return

	def CreateSavedOrder(self, accountID, order):
		print("Method Unimplemented")
		return

	def DeleteSavedOrder(self, accountID, savedOrderID):
		print("Method Unimplemented")
		return

	def GetSavedOrder(self, accountID, savedOrderID):
		print("Method Unimplemented")
		return

	def GetSavedOrderByPath(self, accountID):
		print("Method Unimplemented")
		return

	def ReplacedSavedOrder(self, accountID, savedOrderID, order):
		print("Method Unimplemented")
		return

	def GetAccount(self, accountID, fields):
		print("Method Unimplemented")
		return

	def GetAccounts(self, fields):
		print("Method Unimplemented")
		return

	def PostAccessToken(self, grant_type, refresh_token, access_type, code, client_id, redirect_uri):
		print("Method Unimplemented")
		return
	
	def GetInstrument(self, cusip):
		print("Method Unimplemented")
		return
	'''
	
	def SearchInstruments(self, symbol, projection='fundamental'):
		path = API_CORE_PATH + API_INSTRUMENT_SUFFIX
		
		params = { 'apikey' : API_KEY,
				   'symbol' : symbol,
				   'projection' : projection }
				   
		fullpath = path
		json = SendJSON(fullpath, params)
		
		if not json:
			print("Invalid JSON Parameter")
			self.failedQueries += 1
		else:
			self.successfulQueries += 1
			
			if projection == 'fundamental':
				tmp = instruments.Fundamental(json)
			elif project == 'symbol-search':
				tmp = instruments.Instrument(json)
			else:
				print("Invalid projection type.")
			
			print(tmp.symbol)
		
		return

	# Valid date strings are (1) yyyy-MM-dd (2) yyyy-MM-dd'T'HH:mm:ssz
	def GetMarketHours(self, market, date='0000-00-00'):
		path = API_CORE_PATH + API_MARKETHOURS_SUFFIX
		suffix = "/hours"

		params = { 'apikey' : API_KEY }

		if date != '0000-00-00':
			params['date'] = date

		# Construct full path and sent JSON GET request.
		fullpath = path + market.upper() + suffix
		json = SendJSON(fullpath, params)

		if not json:
			print("Invalid JSON parameter.")
			self.failedQueries		+= 1
		else:
			self.successfulQueries 	+= 1
			idx = market.lower()

			stat = 'Open'
			if json[idx][idx]['isOpen'] == False:
				stat = 'Closed'

			dt = datetime.datetime.now()
			print("---------------------")
			print(json[idx][idx]['marketType'] + " Market Status:")
			print("\tDate: " + json[idx][idx]['date'])
			print("\tTime: " + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second))
			print("\tStatus: " + stat)
			print("---------------------")

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
		json = SendJSON(fullpath, params)

		if not json:
			print("Invalid JSON parameter.")
			self.failedQueries		+= 1
		else:
			self.successfulQueries 	+= 1

			# Display character for change type.
			if change == 'value':
				type = 'U'
			else:
				type = '%'

			# Display all 10 movers.
			ctx = len(json)
			for i in range(0, ctx):
				print("-- [" + direction.upper() + "] --")
				print("Symbol: " + json[i]['symbol'])
				print("Description: " + json[i]['description'])
				print("Change: " + str(json[i]['change']) + type)
				print("Last: $" + str(json[i]['last']) + " Volume: " + str(json[i]['totalVolume']))
				print("----------")

		return deepcopy(json)

	def GetOptionChain(self, symbol, contractType, strikeCount, includeQuotes, strategy, interval, strike, range, fromDate, toDate, volatility, underlyingPrice, interestRate, daysToExp, expMonth, optionType):
		print("Method Unimplemented")
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
					'frequencyType' : ft,
					'frequency' : f,
					'needExtendedHoursData' : 'false' }

		# If start and end times are provided, add them to the parameters. The
		# API specifies that period should then not be provided.
		if endDate != 0 and startDate < endDate:
			params['endDate'] = endDate
			params['startDate'] = startDate
		else:
			params['period'] = p

		# Include extended hours data?
		if extendedHours == True:
			params['needExtendedHoursData'] = 'true'

		argc  = 0
		clist = []

		# Setup full API path and send JSON GET request.
		fullpath = path + symbol + suffix
		json = SendJSON(fullpath, params)

		# If response was empty, something went wrong.
		if not json:
			print("Invalid JSON parameter.")
			self.failedQueries		+= 1
		elif 'error' in list(json.keys()):
			print("Error: " + json['error'])
			self.failedQueries		+= 1
		else:
			self.successfulQueries 	+= 1

			argc = len(json["candles"])

			# Create a candle object for each piece of
			# candle data recieved.
			for i in range(0, argc):
				c = candles.Candle(json["candles"][i])
				clist.append(c)
				c.PrintAttributes()

		print("Retrieved " + str(argc) + " candles.")

		return deepcopy(clist)

	# Symbols is a list of symbols.
	# Returns a list of quotes.
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
			json = SendJSON(fullpath, params)

			# If response was empty, something went wrong.
			if not json:
				print("Invalid symbol name.")
				self.failedQueries		+= 1
			else:
				self.successfulQueries	+= 1
				type = quotes.GetQuoteType(sym, json)

				# For each symbol returned...
				if type == 'EQUITY':
					obj = quotes.EquityQuote(json)
					obj.PrintAttributes()
					quote_array.append(obj)
				elif type == 'MUTUAL_FUND':
					obj = quotes.MutualFundQuote(json)
					obj.PrintAttributes()
					quote_array.append(obj)
				else:
					print(json)

		return deepcopy(quote_array)

	'''
	def GetTransaction(self, accountID, transactionID):
		print("Method Unimplemented")
		return

	def GetTransactions(self, accountID, type, symbol, startDate, endDate):
		print("Method Unimplemented")
		return

	def GetPreferences(self, accountID):
		print("Method Unimplemented")
		return

	def GetSubscriptionKeys(self, accountIDs):
		print("Method Unimplemented")
		return

	def GetUserPrincipals(self, fields):
		print("Method Unimplemented")
		return

	def SetPreferences(self, accountID, preferences):
		print("Method Unimplemented")
		return

	def CreateWatchlist(self, accountID, watchlist):
		print("Method Unimplemented")
		return

	def DeleteWatchlist(self, accountID, watchlistID):
		print("Method Unimplemented")
		return

	def GetWatchlist(self, accountID, watchlistID):
		print("Method Unimplemented")
		return

	def GetWatchlists(self, accountID):
		print("Method Unimplemented")
		return

	def GetAllWatchlists(self):
		print("Method Unimplemented")
		return

	def ReplaceWatchlist(self, accountID, watchlistID, watchlist):
		print("Method Unimplemented")
		return

	def UpdateWatchlist(self, accountID, watchlistID, watchlist):
		print("Method Unimplemented")
		return
	'''

# Send a JSON request given a URL address and JSON parameters.
def SendJSON(address, parameters):
	r = requests.get(url = address, params = parameters)
	data = r.json()

	return data

# Converts ms since epoch to a timestamp string
def StampToString(stamp):
	return

# Converts timestamp string to ms since epoch.
def StringToStamp(string):
	return