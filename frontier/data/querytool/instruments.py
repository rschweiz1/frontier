# Module is an abstraction of instrument data, including fundamental data.
class Instrument(object):
	def __init__(self, json):
		self.type 			= "Instrument"
		self.symbol 		= list(json.keys())[0]
		self.cusip 			= json[self.symbol]['cusip']
		self.description 	= json[self.symbol]['description']
		self.exchange 		= json[self.symbol]['exchange']
		self.assetType 		= json[self.symbol]['assetType']

class Bond(Instrument):
	def __init__(self, json):
		Instrument.__init__(self, json)
		
		self.type 			= "Bond"
		self.price 			= json[self.symbol]['bondPrice']

class Fundamental(Instrument):
	def __init__(self, json):
		Instrument.__init__(self, json)
		
		self.type					= "Fundamental"
		self.week52High 			= json[self.symbol]['fundamental']['high52']
		self.week52Low              = json[self.symbol]['fundamental']['low52']
		self.divAmount              = json[self.symbol]['fundamental']['dividendAmount']
		self.divYield               = json[self.symbol]['fundamental']['dividendYield']
		self.divDate                = json[self.symbol]['fundamental']['dividendDate']
		self.peRatio                = json[self.symbol]['fundamental']['peRatio']
		self.pegRatio               = json[self.symbol]['fundamental']['pegRatio']
		self.pbRatio                = json[self.symbol]['fundamental']['pbRatio']
		self.prRatio                = json[self.symbol]['fundamental']['prRatio']
		self.pcfRatio               = json[self.symbol]['fundamental']['pcfRatio']
		self.grossMarginTTM         = json[self.symbol]['fundamental']['grossMarginTTM']
		self.grossMarginMRQ         = json[self.symbol]['fundamental']['grossMarginMRQ']
		self.netProfitMarginTTM	    = json[self.symbol]['fundamental']['netProfitMarginTTM']
		self.netProfitMarginMRQ     = json[self.symbol]['fundamental']['netProfitMarginMRQ']
		self.operatingMarginTTM     = json[self.symbol]['fundamental']['operatingMarginTTM']
		self.operatingMarginMRQ     = json[self.symbol]['fundamental']['operatingMarginMRQ']
		self.returnOnEquity         = json[self.symbol]['fundamental']['returnOnEquity']
		self.returnOnAssets         = json[self.symbol]['fundamental']['returnOnAssets']
		self.returnOnInvestment     = json[self.symbol]['fundamental']['returnOnInvestment']
		self.quickRatio             = json[self.symbol]['fundamental']['quickRatio']
		self.currentRatio           = json[self.symbol]['fundamental']['currentRatio']
		self.interestCoverage       = json[self.symbol]['fundamental']['interestCoverage']
		self.totalDebtToCapital     = json[self.symbol]['fundamental']['totalDebtToCapital']
		self.ltDebtToEquity         = json[self.symbol]['fundamental']['ltDebtToEquity']
		self.totalDebtToEquity      = json[self.symbol]['fundamental']['totalDebtToEquity']
		self.epsTTM                 = json[self.symbol]['fundamental']['epsTTM']
		self.epsChangePercentTTM    = json[self.symbol]['fundamental']['epsChangePercentTTM']
		self.epsChangeYear          = json[self.symbol]['fundamental']['epsChangeYear']
		self.epsChange              = json[self.symbol]['fundamental']['epsChange']
		self.revChangeYear          = json[self.symbol]['fundamental']['revChangeYear']
		self.revChangeTTM           = json[self.symbol]['fundamental']['revChangeTTM']
		self.revChangeIn            = json[self.symbol]['fundamental']['revChangeIn']
		self.sharesOutstanding      = json[self.symbol]['fundamental']['sharesOutstanding']
		self.marketCapFloat         = json[self.symbol]['fundamental']['marketCapFloat']
		self.marketCap              = json[self.symbol]['fundamental']['marketCap']
		self.bookValuePerShare      = json[self.symbol]['fundamental']['bookValuePerShare']
		self.shortIntToFloat        = json[self.symbol]['fundamental']['shortIntToFloat']
		self.shortIntDayToCover     = json[self.symbol]['fundamental']['shortIntDayToCover']
		self.divGrowthRate3Year     = json[self.symbol]['fundamental']['divGrowthRate3Year']
		self.divPayAmount           = json[self.symbol]['fundamental']['dividendPayAmount']
		self.beta                   = json[self.symbol]['fundamental']['beta']
		self.vol1DayAvg             = json[self.symbol]['fundamental']['vol1DayAvg']
		self.vol10DayAvg            = json[self.symbol]['fundamental']['vol10DayAvg']
		self.vol3MonthAvg           = json[self.symbol]['fundamental']['vol3MonthAvg']