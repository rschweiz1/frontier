# Class to encapsulate user preferences for a TD Ameritrade account.
class UserPreferences(object):
	def __init__(self):
		self.expressTrading = False
		self.directOptionsRouting = False
		self.directEquityRouting = False
		self.defaultEquityOrderLegInstr = ""
		self.defaultEquityOrderType = ""
		self.defaultEquityOrderPriceLinkType = ""
		self.defaultEquityOrderDuration = ""
		self.defaultEquityOrderMarketSession = ""
		self.defaultEquityQuantity = 0
		self.mutualFundTaxLotMethod = ""
		self.optionTaxLotMethod = ""
		self.equityTaxLotMethod = ""
		self.defaultAdvancedToolLaunch = ""
		self.authTokenTimeout = ""