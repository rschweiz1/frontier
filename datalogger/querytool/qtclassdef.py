
# Acts as a superclass to different order types. It contains the interface data all orders share. 
class Order(object):
	def __init__(self, order_data):
		self.session = ""
		self.duration = ""
		self.orderType = ""
		self.cancelTime = ""
		self.shortFormat = False
		self.complexOrderStratType = ""
		self.quantity = 0
		self.filledQuantity = 0
		self.remainingQuantity = 0
		self.requestedDestination = ""
		self.destinationLinkName = ""
		self.releaseTime = ""
		self.stopPrice = -1.0
		self.stopPriceLinkBasis = ""
		self.stopPriceLinkType = ""
		self.stopPriceOffset = -1.0
		self.stopType = ""
		self.priceLinkBasis = ""
		self.priceLinkType = ""
		self.price = -1.0
		self.taxLotMethod = ""
		self.orderLegType = ""
		self.orderLegID = 0
		self.orderLegInstrument = ""
		self.orderLegInstruction = ""
		self.orderLegPositionEffect = ""
		self.orderLegQuantity = 0
		self.orderLegQuantityType = ""
		self.activationPrice = -1.0
		self.specialInstruction = ""
		self.orderStratType = ""
		self.orderID = 0
		self.cancelable = False
		self.editable = False
		self.status = ""
		self.enteredTime = ""
		self.closeTime = ""
		self.tag = ""
		self.accountID = ""
		self.statusDescription = ""
		
		class ExecutionType:
			def __init__(self):
				self.activityType = ""
				self.executionType = "FILL"
				self.quantity = 0
				self.orderRemainingQuantity = 0
				self.execLegID = 0
				self.execLegQuantity = 0
				self.execMismarkedQuantity = 0
				self.execPrice = -1.0
				self.time = ""
			
class OptionOrder(Order):
	def __init__(self, order_data):
		self.assetType = ""
		self.cusip = ""
		self.symbol = ""
		self.description = ""
		self.type = ""
		self.putCall = ""
		self.underlyingSymbol = ""
		self.optionMultiplier = 0
		self.optionSymbol = ""
		self.optionDeliverableUnits = 0
		self.optionCurrencyType = ""
		self.optionAssetType = ""
		
class MutualFundOrder(Order):
	def __init__(self, order_data):
		self.assetType = ""
		self.cusip = ""
		self.symbol = ""
		self.description = ""
		self.type = ""
		
class OptionOrder(Order):
	def __init__(self, order_data):
		self.assetType = ""
		self.cusip = ""
		self.symbol = ""
		self.description = ""
		self.type = ""
		
class CashEquivOrder(Order):
	def __init__(self, order_data):
		self.assetType = ""
		self.cusip = ""
		self.symbol = ""
		self.description = ""
		self.type = ""
		
class EquityOrder(Order):
	def __init__(self, order_data):
		self.assetType = ""
		self.cusip = ""
		self.symbol = ""
		self.description = ""
		
class FixedIncomeOrder(Order):
	def __init__(self, order_data):
		self.assetType = ""
		self.cusip = ""
		self.symbol = ""
		self.description = ""
		self.maturityDate = ""
		self.variableRate = 0
		self.factor = 0

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

class Watchlist(object):
	def __init__(self):
		self.name = ""
		self.watchlistID = ""
		self.watchlistQuantity = 0
		self.watchlistAvgPrice = -1.0
		self.watchlistCommission = -1.0
		self.watchlistPurchasedDate = ""
		self.watchlistSymbol = ""
		self.watchlistAssetType = ""
		self.watchlistSequenceID = 0