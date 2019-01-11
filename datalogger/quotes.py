import argparse

class MutualFund:
	def __init__(self):
		self.symbol = ""
		self.description = ""
		self.closePrice = -1.0
		self.netChange = -1.0
		self.totalVolume = -1.0
		self.tradeTime = -1.0
		self.exchange = ""
		self.exchangeName = ""
		self.digits = -1.0
		self.week52High = -1.0
		self.week52Low = -1.0
		self.nAV = -1.0
		self.peRatio = -1.0
		self.divAmount = -1.0
		self.divYield = -1.0
		self.divDate = ""
		self.securityStatus = ""

class Future:
	def __init__(self):
		self.symbol = ""
		self.bidPrice = -1.0
		self.askPrice = -1.0
		self.lastPrice = -1.0
		self.highPrice = -1.0
		self.lowPrice = -1.0
		self.closePrice = -1.0
		self.exchange = ""
		self.description = ""
		self.openPrice = -1.0
		self.change = -1.0
		self.pctChange = -1.0
		self.exchangeName = ""
		self.digits = -1.0
		self.securityStatus = ""
		self.tick = -1.0
		self.tickAmount = -1.0
		self.product = ""
		self.priceFormat = ""
		self.tradingHours = ""
		self.isTradable = False
		self.multiplier = -1.0
		self.isActive = False
		self.settlementPrice = -1.0
		self.futureActiveSymbol = ""
		self.expirationDate = ""
		
class FutureOption:
	def __init__(self):
		self.symbol = ""
		self.bidPrice = -1.0
		self.askPrice = -1.0
		self.lastPrice = -1.0
		self.highPrice = -1.0
		self.lowPrice = -1.0
		self.closePrice = -1.0
		self.description = -1.0
		self.openPrice = -1.0
		self.netChange = -1.0
		self.openInterest = -1.0
		self.exchangeName = ""
		self.securityStatus = ""
		self.volatility = -1.0
		self.moneyIntValue = -1.0	# Money Intrinsic Value
		self.multiplier = -1.0
		self.digits = -1.0
		self.strikePrice = -1.0
		self.contractType = ""
		self.underlying = ""
		self.timeValue = -1.0
		self.delta = -1.0
		self.gamma = -1.0
		self.theta = -1.0
		self.vega = -1.0
		self.rho = -1.0
		self.mark = -1.0
		self.tick = -1.0
		self.tickAmount - 1.0
		self.isTradable = False
		self.tradingHours = ""
		self.pctChange = -1.0
		self.isActive = False
		self.expirationDate = -1.0
		self.expirationType = ""
		self.exerciseType = ""
		self.inTheMoney = False
		
class Index:
	def __init__(self):
		self.symbol = ""
		self.description = ""
		self.lastPrice = -1.0
		self.openPrice = -1.0
		self.highPrice = -1.0
		self.lowPrice = -1.0
		self.closePrice = -1.0
		self.netChange = -1.0
		self.totalVolume = -1.0
		self.tradeTime = -1.0
		self.exchange = ""
		self.exchangeName = ""
		self.digits = -1.0
		self.week52High = -1.0
		self.week52Low = -1.0
		self.securityStatus = ""
		
class Option:
	def __init__(self):
		self.symbol = ""
		self.description = ""
		self.bidPrice = -1.0
		self.bidSize = -1.0
		self.askPrice = -1.0
		self.askSize = -1.0
		self.lastPrice = -1.0
		self.lastSize = -1.0
		self.openPrice = -1.0
		self.highPrice = -1.0
		self.lowPrice = -1.0
		self.closePrice = -1.0
		self.netChange = -1.0
		self.totalVolume = -1.0
		self.quoteTime = 0
		self.tradeTime = 0
		self.mark = -1.0
		self.openInterest = -1.0
		self.volatility = -1.0
		self.moneyIntValue = -1.0
		self.multiplier = -1.0
		self.strikePrice = -1.0
		self.contractType = ""
		self.underlying = ""
		self.timeValue = -1.0
		self.deliverables = ""
		self.delta = -1.0
		self.gamma = -1.0
		self.theta = -1.0
		self.vega = -1.0
		self.rho = -1.0
		self.securityStatus = ""
		self.theoreticalValue = -1.0
		self.underlyingPrice = -1.0
		self.uvExpirationType = ""
		self.exchange = ""
		self.exchangeName = ""
		self.settlementName = ""
		
class Forex:
	def __init__(self):
		self.symbol = ""
		self.bidPrice = -1.0
		self.askPrice = -1.0
		self.lastPrice = -1.0
		self.highPrice = -1.0
		self.lowPrice = -1.0
		self.closePrice = -1.0
		self.exchange = ""
		self.description = ""
		self.openPrice = -1.0
		self.change = -1.0
		self.pctChange = -1.0
		self.exchangeName = ""
		self.digits = -1.0
		self.securityStatus = ""
		self.tick = -1.0
		self.tickAmount = -1.0
		self.product = ""
		self.tradingHours = ""
		self.isTradable = False
		self.marketMaker = ""
		self.week52High = -1.0
		self.week52Low = -1.0
		self.mark = -1.0
		
class ETF:
	def __init__(self):
		self.symbol = ""
		self.description = ""
		self.bidPrice = -1.0
		self.bidSize = -1.0
		self.bidID = ""
		self.askPrice = -1.0
		self.askSize = -1.0
		self.askID = ""
		self.lastPrice = -1.0
		self.lastSize = -1.0
		self.lastID = ""
		self.openPrice = -1.0
		self.highPrice = -1.0
		self.lowPrice = -1.0
		self.closePrice = -1.0
		self.netChange = -1.0
		self.totalVolume = -1.0
		self.quoteTime = -1.0
		self.tradeTime = -1.0
		self.mark = -1.0
		self.exchange = ""
		self.exchangeName = ""
		self.marginable = False
		self.shortable = False
		self.volatility = -1.0
		self.digits = -1.0
		self.week52High = -1.0
		self.week52Low = -1.0
		self.peRatio = -1.0
		self.divAmount = -1.0
		self.divYield = -1.0
		self.divDate = -1.0
		self.securityStatus = ""
		self.regMarketLastPrice = -1.0
		self.regMarketLastSize = -1.0
		self.regMarketNetChange = -1.0
		self.regMarketTradeTime = 0
		
class Equity:
	def __init__(self):
		self.symbol = ""
		self.description = ""
		self.bidPrice = -1.0
		self.bidSize = -1.0
		self.bidID = ""
		self.askPrice = -1.0
		self.askSize = -1.0
		self.askID = ""
		self.lastPrice = -1.0
		self.lastSize = -1.0
		self.lastID = ""
		self.openPrice = -1.0
		self.highPrice = -1.0
		self.lowPrice = -1.0
		self.closePrice = -1.0
		self.netChange = -1.0
		self.totalVolume = -1.0
		self.quoteTime = -1.0
		self.tradeTime = -1.0
		self.mark = -1.0
		self.exchange = ""
		self.exchangeName = ""
		self.marginable = False
		self.shortable = False
		self.volatility = -1.0
		self.digits = -1.0
		self.week52High = -1.0
		self.week52Low = -1.0
		self.peRatio = -1.0
		self.divAmount = -1.0
		self.divYield = -1.0
		self.divDate = ""
		self.securityStatus = ""
		self.regMarketLastPrice = -1.0
		self.regMarketLastSize = -1.0
		self.regMarketNetChange = -1.0
		self.regMarketTradeTime = 0
			
def Run():
	print "quotes.py"
	return
	
if __name__ == "__main__":
	Run()