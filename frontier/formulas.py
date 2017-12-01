from pandas import read_csv
import numpy as np
import scipy.stats as  ss
import os

# Covariance Calculation

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
