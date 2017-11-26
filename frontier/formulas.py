import numpy as np
import scipy.stats as  ss
from scipy.integrate import quad

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

		for i in range (N):
			print(BlackScholes(Otype,  self.price, self.strike[i], r, sigma, T))


n  = 'Apple'
p  = 157.41
s  = np.array([149.00, 150.00, 152.50, 155.00, 157.50, 160.00, 162.50, 165.00])
ca = np.array([9.65, 8.85, 6.90, 5.25, 3.80, 2.62, 1.69, 1.05])
cb = np.array([9.35, 8.55, 6.70, 5.05, 3.65, 2.54, 1.62, 1.00])
cv = np.array([0, 27, 59, 404, 720, 727, 2134, 805])
pa = np.array([1.17, 1.36, 2.04, 2.96, 4.10, 5.55, 7.20, 9.10])
pb = np.array([1.07, 1.29, 1.95, 2.86, 4.00, 5.35, 7.00, 8.90])
pv = np.array([45, 1500, 31, 317, 604, 229, 32, 70])

r=0.001
sigma = 0.23
T = 1/12
Otype = 'C'
 
AAPL_Nov10_2017 = option(n, p, s, ca, cb, cv, pa, pb, pv)





