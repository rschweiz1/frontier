import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

def gmvp(prtf):
    """Finds the weights of a portfolio for minimum variance."""
    scaler = MinMaxScaler()
    pca = PCA(n_components=10)
    samples = pd.DataFrame()
    e = np.ones(prtf.shape[1])
    for i in range(prtf.shape[0]-252):
        sample = prtf.iloc[i:i+252]
        scaled = scaler.fit_transform(sample)
        v = pca.fit(scaled).get_precision()
        pweights = pd.Series((v@e) / (e@v@e), index=prtf.columns)
        georet = sample.agg('sum').apply(lambda x: np.exp(x) - 1)
        pret = (pweights * georet).sum()
        print(pret)
        samples = samples.append(pweights, ignore_index=True)
    return samples

def scrub(data):
    """
    Reads a CSV file and organizes it neatly into a DataFrame.

    Arguments:
        data {.csv} -- the csv file to be read and scrubbed

    Returns:
        DataFrame -- the logarithmic returns of selected ticker symbols
    """
    df = pd.read_csv(data, header=0, index_col=0, parse_dates=True)
    df.dropna(axis=1, inplace=True)
    logret = np.log(df).diff().iloc[1:]
    return logret

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    """
    Frame a time series as a supervised learning dataset.
    (Adapted from Jason Brownlee's LSTM for multivariate time series)

    Arguments:
        data: Sequence of observations as a list or NumPy array.
        n_in: Number of lag observations as input (X).
        n_out: Number of observations as output (y).

    Returns:
        Pandas DataFrame or series framed for supervised learning.
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
