import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler


def scrub(data):
    df = pd.read_csv(data, header=0, index_col=0, parse_dates=True)
    df.dropna(axis=1, inplace=True)
    logret = np.log(df).diff().iloc[1:]
    scaler = MinMaxScaler(feature_range=(0, 1))
    pca = PCA(n_components=15)
    samples = pd.DataFrame()
    e = np.ones(df.shape[1])
    for i in range(logret.shape[0]-252):
        sample = logret.iloc[i:i+252]
        scaled = scaler.fit_transform(sample)
        v = pca.fit(scaled).get_precision()
        gmvp = pd.Series((v@e) / (e@v@e), index=df.columns)
        georet = sample.agg('sum').apply(lambda x: np.exp(x) - 1)
        pret = (gmvp * georet).sum()
        print(pret)
        samples = samples.append(gmvp, ignore_index=True)
    return samples

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    """
    Frame a time series as a supervised learning dataset.
    Arguments:
        data: Sequence of observations as a list or NumPy array.
        n_in: Number of lag observations as input (X).
        n_out: Number of observations as output (y).
    Returns:
        Pandas DataFrame of series framed for supervised learning.
    (Adapted from Jason Brownlee's LSTM for multivariate time series)
    """
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var{}(t-{})'.format(j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var{}(t)'.format(j+1)) for j in range(n_vars)]
        else:
            names += [('var{}(t+{})'.format(j+1, i)) for j in range(n_vars)]
    # put it all together
    supervised = pd.concat(cols, axis=1)
    supervised.columns = names
    # drop rows with NaN values
    if dropnan:
        supervised.dropna(inplace=True)
    return supervised

# Black-Scholes Formula (adapted from gosmej1977.blogspot.com)
"""NOT CURRENTLY IMPLEMENTED
def d1(S0, K, r, sigma, T):
    return (np.log(S0/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))

def d2(S0, K, r, sigma, T):
    return (np.log(S0/K)+(r-sigma**2/2)*T)/(sigma*np.sqrt(T))

def blackscholes(type, S0, K, r, sigma, T):
    if type=="C":
        return S0*ss.norm.cdf(d1(S0,K,r,sigma,T))-K*np.exp(-r*T)*ss.norm.cdf(d2(S0,K,r,sigma,T))

class option():
    def __init__(self, name, price, strike,
                    callask, callbid, callvol,
                    putask, putbid, putvol):
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
"""
