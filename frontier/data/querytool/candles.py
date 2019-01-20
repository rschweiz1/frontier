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
	
	def GetTimestamp(self):
		""" 
		Method uses the stored datetime, which is stored as
		milliseconds since epoch (1970), and returns a
		human-readable timedate string.
		"""
		years 	= 0
		months 	= 0
		days 	= 0
		hours 	= 0
		minutes = 0
		seconds = 0
		retval 	= ""
		if self.datetime > 0:
			offset = 1546300800000			# Number of ms from epoch to 1-1-2019 @ 0:00:00
			diff = (self.datetime - offset) / 1000
			
		return retval
	
	def PrintAttributes(self):
		print("Time: " + str(self.datetime) + "\tOpen: $" + str(self.openPrice) + "\tClose: $" + str(self.closePrice) + "\tLow: $" + str(self.lowPrice) + "\tHigh: $" + str(self.highPrice) + "\tVolume: " + str(self.volume))