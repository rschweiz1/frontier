# Module is an abstraction of quotes, which is the returned data structure when requesting
# different types of realtime data from the market API.

# This is a superclass for the subclasses following it; it acts as a master quote object.
# The objects are initialized by passing JSON GET data retrieved from the API.
class Quote(object):
	def __init__(self, json):
		self.type			= ""
		self.symbol 		= list(json.keys())[0]
		self.description 	= json[self.symbol]['description']
		self.exchange 		= json[self.symbol]['exchange']
		self.exchangeName 	= json[self.symbol]['exchangeName']
		self.securityStatus = json[self.symbol]['securityStatus']

	def DumpAttributes(self):
		for attr in self.__dict__.keys():
			print(attr + " = " + str(self.__dict__[attr]))

class MutualFundQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "MutualFund"
		self.closePrice 	= json[self.symbol]['closePrice']
		self.netChange 		= json[self.symbol]['netChange']
		self.totalVolume 	= json[self.symbol]['totalVolume']
		self.tradeTime 		= json[self.symbol]['tradeTimeInLong']
		self.digits 		= json[self.symbol]['digits']
		self.week52High 	= json[self.symbol]['52WkHigh']
		self.week52Low 		= json[self.symbol]['52WkLow']
		self.nAV 			= json[self.symbol]['nAV']
		self.peRatio 		= json[self.symbol]['peRatio']
		self.divAmount 		= json[self.symbol]['divAmount']
		self.divYield 		= json[self.symbol]['divYield']
		self.divDate 		= json[self.symbol]['divDate']

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
		self.bidPrice 			= json[self.symbol]['bidPriceInDouble']
		self.askPrice 			= json[self.symbol]['askPriceInDouble']
		self.lastPrice 			= json[self.symbol]['lastPriceInDouble']
		self.bidID				= json[self.symbol]['bidId']
		self.askID				= json[self.symbol]['askId']
		self.highPrice 			= json[self.symbol]['highPriceInDouble']
		self.lowPrice 			= json[self.symbol]['lowPriceInDouble']
		self.closePrice 		= json[self.symbol]['closePriceInDouble']
		self.openPrice 			= json[self.symbol]['openPriceInDouble']
		self.change 			= json[self.symbol]['changeInDouble']
		self.pctChange 			= json[self.symbol]['futurePercentChange']
		self.openInterest		= json[self.symbol]['openInterest']
		self.mark				= json[self.symbol]['mark']
		self.tick 				= json[self.symbol]['tick']
		self.tickAmount 		= json[self.symbol]['tickAmount']
		self.product 			= json[self.symbol]['product']
		self.priceFormat 		= json[self.symbol]['futurePriceFormat']
		self.tradingHours 		= json[self.symbol]['futureTradingHours']
		self.isTradable 		= json[self.symbol]['futureIsTradable']
		self.multiplier 		= json[self.symbol]['futureMultiplier']
		self.isActive 			= json[self.symbol]['futureIsActive']
		self.settlementPrice 	= json[self.symbol]['futureSettlementPrice']
		self.futureActiveSymbol = json[self.symbol]['futureActiveSymbol']
		self.expirationDate 	= json[self.symbol]['futureExpirationDate']

class FutureOptionQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "FutureOption"
		self.bidPrice 		= json[self.symbol]['bidPriceInDouble']
		self.askPrice 		= json[self.symbol]['askPriceInDouble']
		self.lastPrice 		= json[self.symbol]['lastPriceInDouble']
		self.highPrice 		= json[self.symbol]['highPriceInDouble']
		self.lowPrice 		= json[self.symbol]['lowPriceInDouble']
		self.closePrice 	= json[self.symbol]['closePriceInDouble']
		self.openPrice 		= json[self.symbol]['openPriceInDouble']
		self.netChange 		= json[self.symbol]['netChangeInDouble']
		self.openInterest 	= json[self.symbol]['openInterest']
		self.volatility 	= json[self.symbol]['volatility']
		self.moneyIntValue 	= json[self.symbol]['moneyIntrinsicValueInDouble']
		self.multiplier 	= json[self.symbol]['multiplierInDouble']
		self.digits 		= json[self.symbol]['digits']
		self.strikePrice 	= json[self.symbol]['strikePriceInDouble']
		self.contractType 	= json[self.symbol]['contractType']
		self.underlying 	= json[self.symbol]['underlying']
		self.timeValue 		= json[self.symbol]['timeValueInDouble']
		self.delta 			= json[self.symbol]['deltaInDouble']
		self.gamma 			= json[self.symbol]['gammaInDouble']
		self.theta 			= json[self.symbol]['thetaInDouble']
		self.vega 			= json[self.symbol]['vegaInDouble']
		self.rho 			= json[self.symbol]['rhoInDouble']
		self.mark 			= json[self.symbol]['mark']
		self.tick 			= json[self.symbol]['tick']
		self.tickAmount 	= json[self.symbol]['tickAmount']
		self.isTradable 	= json[self.symbol]['futureIsTradable']
		self.tradingHours 	= json[self.symbol]['futureTradingHours']
		self.pctChange 		= json[self.symbol]['futurePercentChange']
		self.isActive 		= json[self.symbol]['futureIsActive']
		self.expirationDate = json[self.symbol]['futureExpirationDate']
		self.expirationType = json[self.symbol]['expirationType']
		self.exerciseType 	= json[self.symbol]['exerciseType']
		self.inTheMoney 	= json[self.symbol]['inTheMoney']

class IndexQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "Index"
		self.lastPrice 		= json[self.symbol]['lastPrice']
		self.openPrice 		= json[self.symbol]['openPrice']
		self.highPrice 		= json[self.symbol]['highPrice']
		self.lowPrice 		= json[self.symbol]['lowPrice']
		self.closePrice 	= json[self.symbol]['closePrice']
		self.netChange 		= json[self.symbol]['netChange']
		self.totalVolume 	= json[self.symbol]['totalVolume']
		self.tradeTime 		= json[self.symbol]['tradeTimeInLong']
		self.digits 		= json[self.symbol]['digits']
		self.week52High 	= json[self.symbol]['52WkHigh']
		self.week52Low 		= json[self.symbol]['52WkLow']

class OptionQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type				= "Option"
		self.bidPrice 			= json[self.symbol]['bidPrice']
		self.bidSize 			= json[self.symbol]['bidSize']
		self.askPrice 			= json[self.symbol]['askPrice']
		self.askSize 			= json[self.symbol]['askSize']
		self.lastPrice 			= json[self.symbol]['lastPrice']
		self.lastSize 			= json[self.symbol]['lastSize']
		self.openPrice 			= json[self.symbol]['openPrice']
		self.highPrice 			= json[self.symbol]['highPrice']
		self.lowPrice 			= json[self.symbol]['lowPrice']
		self.closePrice 		= json[self.symbol]['closePrice']
		self.netChange 			= json[self.symbol]['netChange']
		self.totalVolume 		= json[self.symbol]['totalVolume']
		self.quoteTime 			= json[self.symbol]['quoteTimeInLong']
		self.tradeTime 			= json[self.symbol]['tradeTimeInLong']
		self.mark 				= json[self.symbol]['mark']
		self.openInterest 		= json[self.symbol]['openInterest']
		self.volatility 		= json[self.symbol]['volatility']
		self.moneyIntValue 		= json[self.symbol]['moneyIntrinsicValue']
		self.multiplier 		= json[self.symbol]['multiplier']
		self.strikePrice 		= json[self.symbol]['strikePrice']
		self.contractType 		= json[self.symbol]['contractType']
		self.underlying 		= json[self.symbol]['underlying']
		self.timeValue 			= json[self.symbol]['timeValue']
		self.deliverables 		= json[self.symbol]['deliverables']
		self.delta 				= json[self.symbol]['delta']
		self.gamma 				= json[self.symbol]['gamma']
		self.theta 				= json[self.symbol]['theta']
		self.vega 				= json[self.symbol]['vega']
		self.rho 				= json[self.symbol]['rho']
		self.theoreticalValue 	= json[self.symbol]['theoreticalOptionValue']
		self.underlyingPrice 	= json[self.symbol]['underlyingPrice']
		self.uvExpirationType 	= json[self.symbol]['uvExpirationType']
		self.settlementType 	= json[self.symbol]['settlementType']

class ForexQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type			= "Forex"
		self.bidPrice 		= json[self.symbol]['bidPriceInDouble']
		self.askPrice 		= json[self.symbol]['askPriceInDouble']
		self.lastPrice 		= json[self.symbol]['lastPriceInDouble']
		self.highPrice 		= json[self.symbol]['highPriceInDouble']
		self.lowPrice 		= json[self.symbol]['lowPriceInDouble']
		self.closePrice 	= json[self.symbol]['closePriceInDouble']
		self.openPrice 		= json[self.symbol]['openPriceInDouble']
		self.change 		= json[self.symbol]['changeInDouble']
		self.pctChange 		= json[self.symbol]['percentChange']
		self.digits 		= json[self.symbol]['digits']
		self.tick 			= json[self.symbol]['tick']
		self.tickAmount 	= json[self.symbol]['tickAmount']
		self.product 		= json[self.symbol]['product']
		self.tradingHours 	= json[self.symbol]['tradingHours']
		self.isTradable 	= json[self.symbol]['isTradable']
		self.marketMaker 	= json[self.symbol]['marketMaker']
		self.week52High 	= json[self.symbol]['52WkHighInDouble']
		self.week52Low 		= json[self.symbol]['52WkLowInDouble']
		self.mark 			= json[self.symbol]['mark']

class ETFQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type				= "ETF"
		self.bidPrice 			= json[self.symbol]['bidPrice']
		self.bidSize 			= json[self.symbol]['bidSize']
		self.bidID 				= json[self.symbol]['bidId']
		self.askPrice 			= json[self.symbol]['askPrice']
		self.askSize 			= json[self.symbol]['askSize']
		self.askID 				= json[self.symbol]['askId']
		self.lastPrice 			= json[self.symbol]['lastPrice']
		self.lastSize 			= json[self.symbol]['lastSize']
		self.lastID 			= json[self.symbol]['lastId']
		self.openPrice 			= json[self.symbol]['openPrice']
		self.highPrice 			= json[self.symbol]['highPrice']
		self.lowPrice 			= json[self.symbol]['lowPrice']
		self.closePrice 		= json[self.symbol]['closePrice']
		self.netChange 			= json[self.symbol]['netChange']
		self.totalVolume 		= json[self.symbol]['totalVolume']
		self.quoteTime 			= json[self.symbol]['quoteTimeInLong']
		self.tradeTime 			= json[self.symbol]['tradeTimeInLong']
		self.mark 				= json[self.symbol]['mark']
		self.marginable			= json[self.symbol]['marginable']
		self.shortable 			= json[self.symbol]['shortable']
		self.volatility 		= json[self.symbol]['volatility']
		self.digits 			= json[self.symbol]['digits']
		self.week52High 		= json[self.symbol]['52WkHigh']
		self.week52Low 			= json[self.symbol]['52WkLow']
		self.peRatio 			= json[self.symbol]['peRatio']
		self.divAmount 			= json[self.symbol]['divAmount']
		self.divYield 			= json[self.symbol]['divYield']
		self.divDate 			= json[self.symbol]['divDate']
		self.regMarketLastPrice = json[self.symbol]['regularMarketLastPrice']
		self.regMarketLastSize 	= json[self.symbol]['regularMarketLastSize']
		self.regMarketNetChange = json[self.symbol]['regularMarketNetChange']
		self.regMarketTradeTime = json[self.symbol]['regularMarketTradeTimeInLong']

class EquityQuote(Quote):
	def __init__(self, json):
		Quote.__init__(self, json)

		self.type				= "Equity"
		self.bidPrice 			= json[self.symbol]['bidPrice']
		self.bidSize 			= json[self.symbol]['bidSize']
		self.bidID 				= json[self.symbol]['bidId']
		self.askPrice 			= json[self.symbol]['askPrice']
		self.askSize 			= json[self.symbol]['askSize']
		self.askID 				= json[self.symbol]['askId']
		self.lastPrice 			= json[self.symbol]['lastPrice']
		self.lastSize 			= json[self.symbol]['lastSize']
		self.lastID 			= json[self.symbol]['lastId']
		self.openPrice 			= json[self.symbol]['openPrice']
		self.highPrice 			= json[self.symbol]['highPrice']
		self.lowPrice 			= json[self.symbol]['lowPrice']
		self.closePrice 		= json[self.symbol]['closePrice']
		self.netChange 			= json[self.symbol]['netChange']
		self.totalVolume 		= json[self.symbol]['totalVolume']
		self.quoteTime 			= json[self.symbol]['quoteTimeInLong']
		self.tradeTime 			= json[self.symbol]['tradeTimeInLong']
		self.mark 				= json[self.symbol]['mark']
		self.marginable 		= json[self.symbol]['marginable']
		self.shortable 			= json[self.symbol]['shortable']
		self.volatility 		= json[self.symbol]['volatility']
		self.digits 			= json[self.symbol]['digits']
		self.week52High 		= json[self.symbol]['52WkHigh']
		self.week52Low 			= json[self.symbol]['52WkLow']
		self.peRatio 			= json[self.symbol]['peRatio']
		self.divAmount 			= json[self.symbol]['divAmount']
		self.divYield 			= json[self.symbol]['divYield']
		self.divDate 			= json[self.symbol]['divDate']
		self.regMarketLastPrice = json[self.symbol]['regularMarketLastPrice']
		self.regMarketLastSize 	= json[self.symbol]['regularMarketLastSize']
		self.regMarketNetChange = json[self.symbol]['regularMarketNetChange']
		self.regMarketTradeTime = json[self.symbol]['regularMarketTradeTimeInLong']

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
