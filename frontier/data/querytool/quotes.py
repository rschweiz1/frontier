# Module is an abstraction of quotes, which is the returned data structure when requesting
# different types of realtime data from the market API.

# This is a superclass for the subclasses following it; it acts as a master quote object.
# The objects are initialized by passing JSON GET data retrieved from the API.
class Quote(object):
	def __init__(self, json):
		self.type			= ""
		self.symbol 		= json['symbol']
		self.description 	= json['description']
		self.exchange 		= json['exchange']
		self.exchangeName 	= json['exchangeName']
		self.securityStatus = json['securityStatus']

	def DumpAttributes(self):
		for attr in self.__dict__.keys():
			print(attr + " = " + str(self.__dict__[attr]))

class MutualFundQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "MutualFund"
		self.closePrice 	= json['closePrice']
		self.netChange 		= json['netChange']
		self.totalVolume 	= json['totalVolume']
		self.tradeTime 		= json['tradeTimeInLong']
		self.digits 		= json['digits']
		self.week52High 	= json['52WkHigh']
		self.week52Low 		= json['52WkLow']
		self.nAV 			= json['nAV']
		self.peRatio 		= json['peRatio']
		self.divAmount 		= json['divAmount']
		self.divYield 		= json['divYield']
		self.divDate 		= json['divDate']

	def PrintAttributes(self):
		print("------------------------------------")
		print(self.symbol + "\n" + self.description + "\n")
		print("Close: $" + str(self.closePrice) + "\tChange: " + str(self.netChange))
		print("Volume: " + str(self.totalVolume))
		print("52 Wk High: $" + str(self.week52High) + "\t52 Wk Low: $" + str(self.week52Low))
		print("------------------------------------")

class FutureQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type				= "Future"
		self.bidPrice 			= json['bidPriceInDouble']
		self.askPrice 			= json['askPriceInDouble']
		self.lastPrice 			= json['lastPriceInDouble']
		self.bidID				= json['bidId']
		self.askID				= json['askId']
		self.highPrice 			= json['highPriceInDouble']
		self.lowPrice 			= json['lowPriceInDouble']
		self.closePrice 		= json['closePriceInDouble']
		self.openPrice 			= json['openPriceInDouble']
		self.change 			= json['changeInDouble']
		self.pctChange 			= json['futurePercentChange']
		self.openInterest		= json['openInterest']
		self.mark				= json['mark']
		self.tick 				= json['tick']
		self.tickAmount 		= json['tickAmount']
		self.product 			= json['product']
		self.priceFormat 		= json['futurePriceFormat']
		self.tradingHours 		= json['futureTradingHours']
		self.isTradable 		= json['futureIsTradable']
		self.multiplier 		= json['futureMultiplier']
		self.isActive 			= json['futureIsActive']
		self.settlementPrice 	= json['futureSettlementPrice']
		self.futureActiveSymbol = json['futureActiveSymbol']
		self.expirationDate 	= json['futureExpirationDate']

class FutureOptionQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "FutureOption"
		self.bidPrice 		= json['bidPriceInDouble']
		self.askPrice 		= json['askPriceInDouble']
		self.lastPrice 		= json['lastPriceInDouble']
		self.highPrice 		= json['highPriceInDouble']
		self.lowPrice 		= json['lowPriceInDouble']
		self.closePrice 	= json['closePriceInDouble']
		self.openPrice 		= json['openPriceInDouble']
		self.netChange 		= json['netChangeInDouble']
		self.openInterest 	= json['openInterest']
		self.volatility 	= json['volatility']
		self.moneyIntValue 	= json['moneyIntrinsicValueInDouble']
		self.multiplier 	= json['multiplierInDouble']
		self.digits 		= json['digits']
		self.strikePrice 	= json['strikePriceInDouble']
		self.contractType 	= json['contractType']
		self.underlying 	= json['underlying']
		self.timeValue 		= json['timeValueInDouble']
		self.delta 			= json['deltaInDouble']
		self.gamma 			= json['gammaInDouble']
		self.theta 			= json['thetaInDouble']
		self.vega 			= json['vegaInDouble']
		self.rho 			= json['rhoInDouble']
		self.mark 			= json['mark']
		self.tick 			= json['tick']
		self.tickAmount 	= json['tickAmount']
		self.isTradable 	= json['futureIsTradable']
		self.tradingHours 	= json['futureTradingHours']
		self.pctChange 		= json['futurePercentChange']
		self.isActive 		= json['futureIsActive']
		self.expirationDate = json['futureExpirationDate']
		self.expirationType = json['expirationType']
		self.exerciseType 	= json['exerciseType']
		self.inTheMoney 	= json['inTheMoney']

class IndexQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "Index"
		self.lastPrice 		= json['lastPrice']
		self.openPrice 		= json['openPrice']
		self.highPrice 		= json['highPrice']
		self.lowPrice 		= json['lowPrice']
		self.closePrice 	= json['closePrice']
		self.netChange 		= json['netChange']
		self.totalVolume 	= json['totalVolume']
		self.tradeTime 		= json['tradeTimeInLong']
		self.digits 		= json['digits']
		self.week52High 	= json['52WkHigh']
		self.week52Low 		= json['52WkLow']

class OptionQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type				= "Option"
		self.bidPrice 			= json['bidPrice']
		self.bidSize 			= json['bidSize']
		self.askPrice 			= json['askPrice']
		self.askSize 			= json['askSize']
		self.lastPrice 			= json['lastPrice']
		self.lastSize 			= json['lastSize']
		self.openPrice 			= json['openPrice']
		self.highPrice 			= json['highPrice']
		self.lowPrice 			= json['lowPrice']
		self.closePrice 		= json['closePrice']
		self.netChange 			= json['netChange']
		self.totalVolume 		= json['totalVolume']
		self.quoteTime 			= json['quoteTimeInLong']
		self.tradeTime 			= json['tradeTimeInLong']
		self.mark 				= json['mark']
		self.openInterest 		= json['openInterest']
		self.volatility 		= json['volatility']
		self.moneyIntValue 		= json['moneyIntrinsicValue']
		self.multiplier 		= json['multiplier']
		self.strikePrice 		= json['strikePrice']
		self.contractType 		= json['contractType']
		self.underlying 		= json['underlying']
		self.timeValue 			= json['timeValue']
		self.deliverables 		= json['deliverables']
		self.delta 				= json['delta']
		self.gamma 				= json['gamma']
		self.theta 				= json['theta']
		self.vega 				= json['vega']
		self.rho 				= json['rho']
		self.theoreticalValue 	= json['theoreticalOptionValue']
		self.underlyingPrice 	= json['underlyingPrice']
		self.uvExpirationType 	= json['uvExpirationType']
		self.settlementType 	= json['settlementType']

class ForexQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "Forex"
		self.bidPrice 		= json['bidPriceInDouble']
		self.askPrice 		= json['askPriceInDouble']
		self.lastPrice 		= json['lastPriceInDouble']
		self.highPrice 		= json['highPriceInDouble']
		self.lowPrice 		= json['lowPriceInDouble']
		self.closePrice 	= json['closePriceInDouble']
		self.openPrice 		= json['openPriceInDouble']
		self.change 		= json['changeInDouble']
		self.pctChange 		= json['percentChange']
		self.digits 		= json['digits']
		self.tick 			= json['tick']
		self.tickAmount 	= json['tickAmount']
		self.product 		= json['product']
		self.tradingHours 	= json['tradingHours']
		self.isTradable 	= json['isTradable']
		self.marketMaker 	= json['marketMaker']
		self.week52High 	= json['52WkHighInDouble']
		self.week52Low 		= json['52WkLowInDouble']
		self.mark 			= json['mark']

class ETFQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type				= "ETF"
		self.bidPrice 			= json['bidPrice']
		self.bidSize 			= json['bidSize']
		self.bidID 				= json['bidId']
		self.askPrice 			= json['askPrice']
		self.askSize 			= json['askSize']
		self.askID 				= json['askId']
		self.lastPrice 			= json['lastPrice']
		self.lastSize 			= json['lastSize']
		self.lastID 			= json['lastId']
		self.openPrice 			= json['openPrice']
		self.highPrice 			= json['highPrice']
		self.lowPrice 			= json['lowPrice']
		self.closePrice 		= json['closePrice']
		self.netChange 			= json['netChange']
		self.totalVolume 		= json['totalVolume']
		self.quoteTime 			= json['quoteTimeInLong']
		self.tradeTime 			= json['tradeTimeInLong']
		self.mark 				= json['mark']
		self.marginable			= json['marginable']
		self.shortable 			= json['shortable']
		self.volatility 		= json['volatility']
		self.digits 			= json['digits']
		self.week52High 		= json['52WkHigh']
		self.week52Low 			= json['52WkLow']
		self.peRatio 			= json['peRatio']
		self.divAmount 			= json['divAmount']
		self.divYield 			= json['divYield']
		self.divDate 			= json['divDate']
		self.regMarketLastPrice = json['regularMarketLastPrice']
		self.regMarketLastSize 	= json['regularMarketLastSize']
		self.regMarketNetChange = json['regularMarketNetChange']
		self.regMarketTradeTime = json['regularMarketTradeTimeInLong']

class EquityQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type				= "Equity"
		self.bidPrice 			= json['bidPrice']
		self.bidSize 			= json['bidSize']
		self.bidID 				= json['bidId']
		self.askPrice 			= json['askPrice']
		self.askSize 			= json['askSize']
		self.askID 				= json['askId']
		self.lastPrice 			= json['lastPrice']
		self.lastSize 			= json['lastSize']
		self.lastID 			= json['lastId']
		self.openPrice 			= json['openPrice']
		self.highPrice 			= json['highPrice']
		self.lowPrice 			= json['lowPrice']
		self.closePrice 		= json['closePrice']
		self.netChange 			= json['netChange']
		self.totalVolume 		= json['totalVolume']
		self.quoteTime 			= json['quoteTimeInLong']
		self.tradeTime 			= json['tradeTimeInLong']
		self.mark 				= json['mark']
		self.marginable 		= json['marginable']
		self.shortable 			= json['shortable']
		self.volatility 		= json['volatility']
		self.digits 			= json['digits']
		self.week52High 		= json['52WkHigh']
		self.week52Low 			= json['52WkLow']
		self.peRatio 			= json['peRatio']
		self.divAmount 			= json['divAmount']
		self.divYield 			= json['divYield']
		self.divDate 			= json['divDate']
		self.regMarketLastPrice = json['regularMarketLastPrice']
		self.regMarketLastSize 	= json['regularMarketLastSize']
		self.regMarketNetChange = json['regularMarketNetChange']
		self.regMarketTradeTime = json['regularMarketTradeTimeInLong']

	def PrintAttributes(self):
		print("--------------------------------")
		print(self.symbol + "\n" + self.description + "\n")
		print("Open: $" + str(self.openPrice) + "\t\tClose: $" + str(self.closePrice))
		print("Low: $" + str(self.lowPrice) + "\t\tHigh: $" + str(self.highPrice))
		print("Volume: " + str(self.totalVolume) + "\tPE Ratio: " + str(self.peRatio))
		print("52 Wk High: $" + str(self.week52High) + "\t52 Wk Low: $" + str(self.week52Low))
		print("--------------------------------")

def GetQuoteType(symbol, raw):
	return raw[symbol]['assetType']
