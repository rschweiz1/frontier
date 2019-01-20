# Module is an abstraction of a candle, which is the data structure returned when requesting price history
# data from the API. It also contains methods for analysis.

class Candle(object):
	def __init__(self, json):
		self.openPrice 		= json['open']
		self.closePrice		= json['close']
		self.lowPrice		= json['low']
		self.highPrice		= json['high']
		self.volume			= json['volume']
		self.datetime		= json['datetime']
	
	def PrintAttributes(self):
		print("Time: " + str(self.datetime) + "\tOpen: $" + str(self.openPrice) + "\tClose: $" + str(self.closePrice) + "\tLow: $" + str(self.lowPrice) + "\tHigh: $" + str(self.highPrice) + "\tVolume: " + str(self.volume))