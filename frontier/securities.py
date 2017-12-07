import pandas as pd
import numpy as np
import pandas_datareader.data as web
import os
from numpy.linalg import inv

def ETF(tickers, group, source = 'google'):

	path = os.path.join(os.path.dirname(__file__),
	'..', 'database', '{}'.format(group), '{}.csv'.format(tickers))

# Datareader retreives historical prices from google finance.
	p = web.DataReader(tickers, source)
	logret = np.log(p.loc['Close']).diff()
	grouped = logret.groupby(pd.Grouper(freq = 'BM'))
	e = np.ones(logret.shape[1])
	f = lambda x: inv(x.cov()) @ e
	g = lambda x: pd.Series(x / (e @ x), index = logret.columns)
	pweights = grouped.apply(f).apply(g)
	georet = grouped.agg(lambda x: x.mean()-x.var()/2)
	scores = pweights * georet
	print(scores)
