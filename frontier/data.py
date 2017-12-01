import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime, os

def Share(ticker, group, source = 'google'):

# tpath is the path to the ticker symbol folder

	tpath = os.path.join(os.path.dirname(__file__),
	'..', 'database', '{}'.format(group), '{}.csv'.format(ticker))

# Datareader retreives historical prices from google finance.

	name = web.DataReader(ticker, source)
	pchange = name['Close'].pct_change().rename('{} Percent Change'.format(ticker))

# Add a percent change column to the DataFrame

	name = pd.concat([name, pchange], axis = 1)
	name.to_csv(tpath)
	return pchange
