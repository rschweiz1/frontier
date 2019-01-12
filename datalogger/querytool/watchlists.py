# Watchlist class.
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