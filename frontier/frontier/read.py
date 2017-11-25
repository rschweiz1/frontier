import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017, 5, 20)
end = datetime.datetime(2017, 7, 14)

def stock(ticker, start, end, source = 'google'):
	return web.DataReader(ticker, source, start, datetime.datetime(2017, 7, 14))

aapl = stock('AAPL', start, end)

print(aapl, start, end)