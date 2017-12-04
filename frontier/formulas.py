import numpy as np
import pandas as pd
import os

def Alpha(group):
	df = pd.read_csv(os.path.join(os.path.dirname(__file__),
	'..', 'database', '{}'.format(group), 'Compiled Data.csv'))
	f = lambda x: np.prod(x+1) - 1 - np.std(x)/2
	df.Date = pd.to_datetime(df.Date)
	df.set_index('Date', inplace = True)
	qcorr = df.groupby(pd.Grouper(freq = 'BQ')).corr()

	qcorr.to_csv(os.path.join(os.path.dirname(__file__),
	'..', 'database', 'machine data', 'Correlation By Quarter.csv'))

	df = df.resample('BQ').apply(f)

	df.to_csv(os.path.join(os.path.dirname(__file__),
	'..', 'database', 'machine data', 'Quarterly Geometric Mean.csv'))


# Black-Scholes Formula (adapted from gosmej1977.blogspot.com)
def d1(S0, K, r, sigma, T):
	return (np.log(S0/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))

def d2(S0, K, r, sigma, T):
	return (np.log(S0/K)+(r-sigma**2/2)*T)/(sigma*np.sqrt(T))

def BlackScholes(type, S0, K, r, sigma, T):
	if type=="C":
		return S0*ss.norm.cdf(d1(S0,K,r,sigma,T))-K*np.exp(-r*T)*ss.norm.cdf(d2(S0,K,r,sigma,T))

class option():
	def __init__(self, name, price, strike, callask, callbid, callvol, putask, putbid, putvol):
		self.name    = n
		self.price   = p
		self.strike  = s
		self.callask = ca
		self.callbid = cb
		self.callvol = cv
		self.putask  = pa
		self.putbid  = pb
		self.putvol  = pv

		N = self.strike.size
