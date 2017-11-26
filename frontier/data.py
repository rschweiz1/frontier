import pandas_datareader.data as web
import datetime, os



def Share(ticker, source = 'google'):
	return web.DataReader(ticker, source).to_csv(os.path.join(os.path.dirname(__file__), '..', 'database', 'ticker' + '.csv'))

def Option(ticker, source = 'google'):
	name = web.Options(ticker, source)
	#return name.get_all_data()

#def Update():
	# Get most recent date of share csv file (pandas.read_csv)
	# Use share function from day after to pre
