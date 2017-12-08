import os
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from numpy.linalg import inv


def gmvp(tickers,
		start='1/1/2010',
		end=pd.to_datetime('today'),
		source='google'):
	"""
	Determines the portfolio's optimal asset weights for minimum variance.

	This formula is based off the proof that a portfolio's variance over time is
	based solely off of the covariance matrix of it's underlying assets. This
	method calculates the optimal weights, and theoretical returns, of any
	combination of assets within the given time span.
	"""
	p = web.DataReader(tickers, source, start, end)

	logret = np.log(p.loc['Close']).diff()
	grouped = logret.groupby(pd.Grouper(freq='BY'))

	e = np.ones(logret.shape[1])

	def f(x): return inv(x.cov()) @ e

	def g(x): return pd.Series(x / (e @ x), index=logret.columns)

	pweights = grouped.apply(f).apply(g)
	georet = grouped.agg('sum').apply(lambda x: np.exp(x) - 1)

	pret = (pweights * georet).sum(axis=1)

	print(
		'Estimated Return:\n{}\nPortfolio Weights:\n{}'.format(pret, pweights))


# Black-Scholes Formula (adapted from gosmej1977.blogspot.com)
def d1(S0, K, r, sigma, T):
	return (np.log(S0/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))

def d2(S0, K, r, sigma, T):
	return (np.log(S0/K)+(r-sigma**2/2)*T)/(sigma*np.sqrt(T))

def blackscholes(type, S0, K, r, sigma, T):
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
