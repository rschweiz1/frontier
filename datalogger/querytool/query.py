import argparse
import requests
import qtclassdef
import quotes

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
		
	def SearchInstruments(self, apikey, symbol, projection):
		print "Method Unimplemented"
		return
		
	def GetInstrument(self, cusip, apikey):
		print "Method Unimplemented"
		return
		
	def GetMarketHours(self, apikey, markets, date):
		print "Method Unimplemented"
		return
		
	def GetMovers(self, index, apikey, direction, change):
		print "Method Unimplemented"
		return
		
	def GetOptionChain(self, apikey, symbol, contractType, strikeCount, includeQuotes, strategy, interval, strike, range, fromDate, toDate, volatility, underlyingPrice, interestRate, daysToExp, expMonth, optionType):
		print "Method Unimplemented"
		return
		
	def GetPriceHistory(self, symbol, apikey, periodType, period, frequencyType, frequency, endDate, startDate, extendedHours):
		print "Method Unimplemented"
		return
		
	def GetQuotes(self, symbols):
		path   = API_CORE_PATH + API_QUOTE_SUFFIX
		suffix = "/quotes"
		params = { 'apikey' : API_KEY }
		
		quotes = []
		
		for sym in symbols:
			
			# Construct full API path.
			fullpath = path + sym + suffix
			
			# Send JSON GET request.
			temp = SendJSON(fullpath, params)
			
			# Get the quote type and create
			# the applicable object.
			type = quotes.GetQuoteType(sym, temp)
			
			if type == 'EQUITY':
				obj = quotes.EquityQuote(temp)
				
				print obj.description
		
		return
		
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
		
def SendJSON(address, parameters):
	r = requests.get(url = address, params = parameters)
	data = r.json()
	
	return data