import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime, os

def Share(ticker, group, source = 'google'):
	asset= {'JKD': 'US Large-Cap Balanced',
	    	'IJH': 'US Mid-Cap Balanced',
	   		'IJR': 'US Small-Cap Balanced',
	   		'JKF': 'US Large-Cap Value',
    		'IJS': 'US Small-Cap Value',
	        'ICF': 'US Real Estate',
	   		'EFA': 'International Large-Cap',
	       	'SCZ': 'International Small-Cap',
	   		'EEM': 'Emerging Markets',
	        'SHV': 'Treasury Short-Term',
	       	'IAU': 'Gold'}

	tpath = os.path.join(os.path.dirname(__file__),
	'..', 'database', '{}'.format(group), '{}.csv'.format(ticker))

# Datareader retreives historical prices from google finance.
	name = web.DataReader(ticker, source)
	name.to_csv(tpath)
	return name['Close'].pct_change().rename('{}'.format(asset[ticker]))
